# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlg_streams.ui'
#
# Created: Wed Sep 28 14:49:49 2016
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Streams(object):
    def setupUi(self, Streams):
        Streams.setObjectName(_fromUtf8("Streams"))
        Streams.resize(480, 266)
        Streams.setMinimumSize(QtCore.QSize(372, 266))
        Streams.setMaximumSize(QtCore.QSize(591, 397))
        self.button_box = QtGui.QDialogButtonBox(Streams)
        self.button_box.setGeometry(QtCore.QRect(200, 230, 161, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.label = QtGui.QLabel(Streams)
        self.label.setGeometry(QtCore.QRect(40, 50, 171, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboDEM = QtGui.QComboBox(Streams)
        self.comboDEM.setGeometry(QtCore.QRect(250, 50, 211, 20))
        self.comboDEM.setObjectName(_fromUtf8("comboDEM"))
        self.formLayoutWidget = QtGui.QWidget(Streams)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 180, 331, 21))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.formLayoutWidget_2 = QtGui.QWidget(Streams)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(30, 10, 291, 31))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_4 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_4)
        self.verticalLayoutWidget = QtGui.QWidget(Streams)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 201, 31))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(Streams)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 80, 201, 31))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.comboFAC = QtGui.QComboBox(Streams)
        self.comboFAC.setGeometry(QtCore.QRect(250, 90, 211, 20))
        self.comboFAC.setObjectName(_fromUtf8("comboFAC"))
        self.label_5 = QtGui.QLabel(Streams)
        self.label_5.setGeometry(QtCore.QRect(40, 90, 171, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayoutWidget_4 = QtGui.QWidget(Streams)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(30, 120, 201, 31))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_6 = QtGui.QLabel(Streams)
        self.label_6.setGeometry(QtCore.QRect(40, 130, 191, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.FAC_Threshold = QtGui.QDoubleSpinBox(Streams)
        self.FAC_Threshold.setGeometry(QtCore.QRect(250, 130, 101, 21))
        self.FAC_Threshold.setDecimals(0)
        self.FAC_Threshold.setMinimum(0.0)
        self.FAC_Threshold.setMaximum(100000.0)
        self.FAC_Threshold.setSingleStep(100.0)
        self.FAC_Threshold.setProperty("value", 1000.0)
        self.FAC_Threshold.setObjectName(_fromUtf8("FAC_Threshold"))

        self.retranslateUi(Streams)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), Streams.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), Streams.reject)
        QtCore.QMetaObject.connectSlotsByName(Streams)

    def retranslateUi(self, Streams):
        Streams.setWindowTitle(_translate("Streams", "StreamWindow", None))
        self.label.setText(_translate("Streams", "Input : Conditioned DEM", None))
        self.label_2.setText(_translate("Streams", "The output stream files are created in the current project folder.", None))
        self.label_4.setText(_translate("Streams", "Perform Stream Delination:", None))
        self.label_5.setText(_translate("Streams", "Input : Flow Accumulation", None))
        self.label_6.setText(_translate("Streams", "Input : Flow Accumulation Threshold", None))

