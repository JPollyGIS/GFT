# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LecoS
                                 A QGIS plugin
 Contains analytical functions for landscape analysis
                             -------------------
        begin                : 2012-09-06
        copyright            : (C) 2013 by Martin Jung
        email                : martinjung at zoho.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import PyQT bindings
from PyQt4.QtCore import *
#from PyQt4.QtCore import QToolBar
from PyQt4.QtGui import *

# Import QGIS analysis tools
from qgis.core import *
from qgis.gui import *
#from qgis.analysis import *

# Import base libraries
import os,sys,csv,string,math,operator,subprocess,tempfile,inspect, time
from os import path

# Import functions and metrics
import lecos_functions as func
import landscape_statistics as lcs
import landscape_polygonoverlay as pov
import landscape_modifier as lmod

import processing, os, subprocess

# Import numpy and scipy
import numpy
try:
    import scipy
except ImportError:
    QMessageBox.critical(QDialog(),"GFT: Warning","Please install scipy (http://scipy.org/) in your QGIS python path.")
    sys.exit(0)
from scipy import ndimage # import ndimage module seperately for easy access

# Import GDAL and ogr
try:
    from osgeo import gdal
except ImportError:
    import gdal
try:
    from osgeo import ogr
except ImportError:
    import ogr

# Register gdal and ogr drivers
#if hasattr(gdal,"AllRegister"): # Can register drivers
#    gdal.AllRegister() # register all gdal drivers
#if hasattr(ogr,"RegisterAll"):
#    ogr.RegisterAll() # register all ogr drivers

# import Ui
from ui.dlg_study_area import Ui_ClipMultipleLayers
from ui.dlg_streams import Ui_Streams
from ui.dlg_Editor import Ui_Editor
from ui.dlg_rel_DEM import Ui_RelativeDEM
from ui.dlg_flow_estimator import Ui_DrainageChannelFlowEstimatorDialogBase
#from ui.dlg_LandscapeModifier import Ui_LandMod

tmpdir = tempfile.gettempdir()

## CODE START ##
# create the dialog controls and set up the user interface from Designer.
class StudyDialog(QDialog, Ui_ClipMultipleLayers):
    def __init__(self, iface):
        # Initialize the Dialog
        QDialog.__init__( self )
        self.setupUi(self)
        self.iface = iface
        
        layers = QgsMapLayerRegistry.instance().mapLayers().values()
        for layer in layers:
            if layer.type() == QgsMapLayer.VectorLayer and layer.wkbType() == QGis.WKBPolygon :
                self.comboBox.addItem( layer.name(), layer ) 
        
        index = self.comboBox.currentIndex()
        selection = self.comboBox.itemData(index)
        
        if selection == None:
            iface.messageBar().pushMessage("Error", "Add a polygon Shapefile the map. The area should represent the intended study area.", level=QgsMessageBar.CRITICAL)
        
        if selection != None:
            
            result = self.exec_()
            if result:
                
                legend = iface.legendInterface()
                layers = iface.legendInterface().layers()
                
                #find the path of the project
                path_project = QgsProject.instance().fileName()
                path_project = path_project[:path_project.rfind("/"):]
                
                #search existence of output folder, if not create it
                directory = path_project + "/output/vectors"
                if not os.path.exists(directory):
                    os.makedirs(directory)
                    
                directory = path_project + "/output/rasters"
                if not os.path.exists(directory):
                    os.makedirs(directory)
                
                #clip part
                for layer in layers  :
                    #clip vector layer (if displayed)
                    if layer.type() == QgsMapLayer.VectorLayer and layer != selection and legend.isLayerVisible(layer) == True :
                        output = path_project + "/output/vectors/Study_Area_" + layer.name() + ".shp"
                        processing.runalg("qgis:intersection",layer,selection,output)
                        
                        # add layer to the legend
                        wb = QgsVectorLayer(output, "Study_Area_" + layer.name(), 'ogr') 
                        if wb.isValid():
                             QgsMapLayerRegistry.instance().addMapLayer(wb)
                    
                    
                    #clip raster layer (if displayed)
                    if layer.type() == QgsMapLayer.RasterLayer and legend.isLayerVisible(layer) == True :
                        output = path_project + "/output/rasters/Study_Area_" + layer.name() + ".tif"
                        command_cut = "gdalwarp -ot Float32 -q -of GTiff -cutline %s -co COMPRESS=NONE %s %s " % ( selection.source(), layer.source(), output )
                        subprocess.call(command_cut)
                        
                        # add layer to the legend
                        wb = QgsRasterLayer(output, "Study_Area_" + layer.name()) 
                        if wb.isValid():
                             QgsMapLayerRegistry.instance().addMapLayer(wb)

class StreamsDialog(QDialog, Ui_Streams):
    def __init__(self, iface):
        # Initialize the Dialog
        QDialog.__init__( self )
        self.setupUi(self)
        self.iface = iface
        
        layers = QgsMapLayerRegistry.instance().mapLayers().values()
        for layer in layers:
            if layer.type() == QgsMapLayer.RasterLayer:
                self.comboDEM.addItem( layer.name(), layer ) 
                self.comboFAC.addItem( layer.name(), layer ) 
                
                #Need to set Thresh FAC_Threshold
                
        index = self.comboDEM.currentIndex()
        DEM = self.comboDEM.itemData(index)
        
        index2 = self.comboFAC.currentIndex()
        FAC = self.comboFAC.itemData(index2)
        
        if DEM == None:
            iface.messageBar().pushMessage("Error", "Add conditioned DEM to the map.", level=QgsMessageBar.CRITICAL)
        
        if DEM != None:
            
            result = self.exec_()
            if result:
                
                #find the path of the project
                path_project = QgsProject.instance().fileName()
                path_project = path_project[:path_project.rfind("/"):]
                
                #runalg inputs
                conddem = func.getRasterLayerByName( self.comboDEM.currentText() )
                conddemPath = conddem.source()
                
                flowacc = func.getRasterLayerByName( self.comboFAC.currentText() )
                flowaccPath = flowacc.source()
                minFlow = self.FAC_Threshold.value()
                
                # Define the minimum extent of the region
                # Not in the help, but need to set an extent
                # http://gis.stackexchange.com/questions/210922/error-running-grass-module-in-qgis-python-console
                rlayer = QgsRasterLayer(conddemPath, str(conddem) + ".tif")
                extent = rlayer.extent()
                xmin = extent.xMinimum()
                xmax = extent.xMaximum()
                ymin = extent.yMinimum()
                ymax = extent.yMaximum()
                
                outStreamIDRas = path_project + "/output/rasters/Study_Area_StreamIDRas" + ".tif"
                outStreamIDVect = path_project + "/output/rasters/Study_Area_StreamIDVect" + ".shp"
                outFlowDir = path_project + "/output/rasters/Study_Area_FlowDir" + ".tif"
                
                # Run the process
                QgsMessageLog.logMessage('Running the stream extract', 'MyPlugin')
               
               
               #Delete files if exist, muct remove from the map 
#                 if os.path.isfile(conddemPath):
#                    os.remove(conddemPath)
#                 if os.path.isfile(flowaccPath):
#                    os.remove(flowaccPath)
                          
                # Run the stream extract
                processing.runalg("grass7:r.stream.extract",conddemPath,
                    flowaccPath,
                    None,minFlow,0,0,0,"%f,%f,%f,%f"% (xmin, xmax, ymin, ymax),0,0,
                    outStreamIDRas,
                    outStreamIDVect,
                    outFlowDir)
                
                # Run the conversion to vector
                outStreamVec = path_project + "/output/rasters/Study_Area_Streams" + ".shp"
                processing.runalg("grass7:r.to.vect", outStreamIDRas,
                                  0,False,"%f,%f,%f,%f"% (xmin, xmax, ymin, ymax),0,outStreamVec)
                
                # Dissolve on the ID
                outStreamVecDiss = path_project + "/output/rasters/Study_Area_Streams_Dissolve" + ".shp"
                processing.runalg("qgis:dissolve",outStreamVec,False,"value",
                                  outStreamVecDiss)
                
                # Add the stream layer to the legend
                wb = QgsVectorLayer(outStreamVecDiss, "Study_Area_Streams", 'ogr') 
                if wb.isValid():
                     QgsMapLayerRegistry.instance().addMapLayer(wb)

class EditDialog(QDialog, Ui_Editor):
    def __init__(self, iface):
        # Initialize the Dialog
        QDialog.__init__( self )
        self.setupUi(self)
        self.iface = iface
        
        result = self.exec_()
        if result:
            self.iface.digitizeToolBar().setVisible(True)
            
class RelDEMDialog(QDialog, Ui_RelativeDEM):
    def __init__(self, iface):
        # Initialize the Dialog
        # Initialize the Dialog
        QDialog.__init__( self )
        self.setupUi(self)
        self.iface = iface
        
        layers = QgsMapLayerRegistry.instance().mapLayers().values()
        for layer in layers:
            if layer.type() == QgsMapLayer.VectorLayer and layer.wkbType() == QGis.WKBLineString :
                self.comboBox.addItem( layer.name(), layer ) 
        
        index = self.comboBox.currentIndex()
        selection = self.comboBox.itemData(index)
        
        if selection == None:
            iface.messageBar().pushMessage("Error", "Add the edited streams layer to the map.", level=QgsMessageBar.CRITICAL)
        
        if selection != None:
            
            result = self.exec_()
            if result:
                
                legend = iface.legendInterface()
                layers = iface.legendInterface().layers()
                
                #find the path of the project
                path_project = QgsProject.instance().fileName()
                path_project = path_project[:path_project.rfind("/"):]
                
                #search existence of output folder, if not create it
                directory = path_project + "/output/vectors"
                directory = path_project + "/output/rasters"
                
                #clip part
                for layer in layers  :
                    #clip vector layer (if displayed)
                    if layer.type() == QgsMapLayer.VectorLayer and layer != selection and legend.isLayerVisible(layer) == True :
                        output = path_project + "/output/vectors/Study_Area_" + layer.name() + ".shp"

                    #clip raster layer (if displayed)
                    if layer.type() == QgsMapLayer.RasterLayer and legend.isLayerVisible(layer) == True :
                        output = path_project + "/output/rasters/Study_Area_" + layer.name() + ".tif"

                            
class FlowDialog(QDialog, Ui_DrainageChannelFlowEstimatorDialogBase):
    def __init__(self, iface):

        # Initialize the Dialog
        QDialog.__init__( self )
        self.setupUi(self)
        self.iface = iface

