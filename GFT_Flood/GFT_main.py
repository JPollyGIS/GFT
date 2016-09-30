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
from PyQt4.QtGui import *

# Import QGIS analysis tools
from qgis.core import *
from qgis.gui import *
#from qgis.analysis import *

# Import base libraries
import os,sys,csv,string,math,operator,subprocess,tempfile,inspect

# Initialize Qt resources from file resources_rc.py
from ui import resources_rc
# Import the code for the dialogs
from GFT_dlg import StudyDialog

# Import the code for the dialogs
from GFT_dlg import StreamsDialog

# Import the code for the dialogs
from GFT_dlg import EditDialog

# Import the code for the dialogs
from GFT_dlg import RelDEMDialog

# Import Batch Dialog
from GFT_dlg import FlowDialog
# Import RasterModifier Dialog
#from lecos_dlg import LandMod

# Import functions for about Dialog
#JSP turn off for now
#import lecos_functions as func

## CODE START ##
class GFT_Flood( object ):
    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        
        # initialize plugin directory
        self.plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/GFT_Flood"
        
        # initialize SEXTANTE support if available
        # jsp turn of support
#         self.sex_load = True
#         self.initSextante()

    def initGui(self):
        # Create action that will start the Study Area
        self.actionStudy = QAction(QIcon(self.plugin_dir+"/icons/icon.png"),\
            u"Study Area", self.iface.mainWindow())
        QObject.connect(self.actionStudy, SIGNAL("triggered()"), self.run)
        
        # Create action that will start the Stream
        self.actionStreams = QAction(QIcon(self.plugin_dir+"/icons/stream.png"),\
            u"Streams", self.iface.mainWindow())
        QObject.connect(self.actionStreams, SIGNAL("triggered()"), self.runStreams)
        
        # Create action for editing streams
        self.actionEditor = QAction(QIcon(self.plugin_dir+"/icons/editor.png"),\
            u"Edit Streams", self.iface.mainWindow())
        QObject.connect(self.actionEditor, SIGNAL("triggered()"), self.editStreams)
        
        # Create action for editing streams
        self.actionRelDEM = QAction(QIcon(self.plugin_dir+"/icons/dem.png"),\
            u"Relative DEM", self.iface.mainWindow())
        QObject.connect(self.actionRelDEM, SIGNAL("triggered()"), self.runRelDEM)
        
        # Create action for small batch dialog
        self.actionFlow = QAction(QIcon(self.plugin_dir+"/icons/icon_batchCover.png"),\
            u"Flow Estimate", self.iface.mainWindow())
        QObject.connect(self.actionFlow, SIGNAL("triggered()"), self.runFlow)
        
        # check if Raster menu available
        if hasattr(self.iface, "addPluginToRasterMenu"):
            self.iface.addPluginToRasterMenu("&GFT", self.actionStudy)
            self.iface.addPluginToRasterMenu("&GFT", self.actionStreams)
            self.iface.addPluginToRasterMenu("&GFT", self.actionEditor)
            self.iface.addPluginToRasterMenu("&GFT", self.actionRelDEM)
            self.iface.addPluginToRasterMenu("&GFT", self.actionFlow)
        else:
            # no menu, place plugin under Plugins menu and toolbox as usual
            self.iface.addPluginToMenu(u"&GFT", self.actionStudy)
            self.iface.addPluginToMenu(u"&GFT", self.actionStreams)
            self.iface.addPluginToMenu(u"&GFT", self.actionEditor)
            self.iface.addPluginToMenu(u"&GFT", self.actionRelDEM)
            self.iface.addPluginToMenu(u"&GFT", self.actionFlow)
            
    def unload(self):
        # check if Raster menu available and remove our buttons from appropriate
        if hasattr(self.iface, "addPluginToRasterMenu"):
            self.iface.removePluginRasterMenu("&GFT",self.actionStudy)
            self.iface.removePluginRasterMenu("&GFT",self.actionStreams)
            self.iface.removePluginRasterMenu("&GFT",self.actionEditor)
            self.iface.removePluginRasterMenu("&GFT",self.actionRelDEM)
            self.iface.removePluginRasterMenu("&GFT",self.actionFlow)  
        else:
            # Remove the plugin menu item and icon
            self.iface.removePluginMenu(u"&GFT",self.actionStudy)
            self.iface.removePluginMenu(u"&GFT",self.actionStreams)
            self.iface.removePluginMenu(u"&GFT",self.actionEditor)
            self.iface.removePluginMenu(u"&GFT",self.actionRelDEM)
            self.iface.removePluginMenu(u"&GFT",self.actionFlow)            
                
    # Try to enable SEXTANTE support if installed
    # JSP turn of support for now
#     def initSextante(self):
#         # Try to import Sextante
#         try:
#             from processing.core.Processing import Processing
#         except ImportError:
#             self.sex_load = False
#         if self.sex_load:
#             # Add folder to sys.path
#             cmd_folder = os.path.split(inspect.getfile( inspect.currentframe() ))[0]
#             if cmd_folder not in sys.path:
#                 sys.path.insert(0, cmd_folder)
#             
#             # Load Lecos Sextante Provider
#             from lecos_sextanteprov import LecoSAlgorithmsProv
#             
#             self.provider = LecoSAlgorithmsProv() # Load LecoS Algorithm Provider
#             Processing.addProvider(self.provider,updateList=True)
        
    # run method that performs all the real work
    def run(self):
        # create and show the dialog
        dlg = StudyDialog( self.iface )
        # show the dialog
        dlg.show()
        #Using exec within dlg class
        #result = dlg.exec_()
    
        # run method that performs all the real work
    def runStreams(self):
        # create and show the dialog
        dlg = StreamsDialog( self.iface )
        # show the dialog
        dlg.show()
        #result = dlg.exec_()
        #Using exec within dlg class
        #result = dlg.exec_(
    def editStreams(self):
        # create and show the dialog
        dlg = EditDialog( self.iface )
        # show the dialog
        dlg.show()
        #result = dlg.exec_()
    def runRelDEM(self):
        # create and show the dialog
        dlg = RelDEMDialog( self.iface )
        # show the dialog
        dlg.show()
        #result = dlg.exec_()
        #Using exec within dlg class
        #result = dlg.exec_()
    
    # Executes small Diversity gui
    def runFlow(self):
        dlg = FlowDialog( self.iface )
        dlg.show()
        #dlg.overrideWindowFlags(Qt.WA_DeleteOnClose)
        result = dlg.exec_()
        
