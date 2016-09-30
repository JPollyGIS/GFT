# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlg_rel_DEM.ui'
#
# Created: Fri Sep 30 11:34:46 2016
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

class Ui_RelativeDEM(object):
    def setupUi(self, RelativeDEM):
        RelativeDEM.setObjectName(_fromUtf8("RelativeDEM"))
        RelativeDEM.resize(513, 266)
        RelativeDEM.setMinimumSize(QtCore.QSize(372, 266))
        RelativeDEM.setMaximumSize(QtCore.QSize(589, 392))
        self.button_box = QtGui.QDialogButtonBox(RelativeDEM)
        self.button_box.setGeometry(QtCore.QRect(180, 220, 161, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.label_2 = QtGui.QLabel(RelativeDEM)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 411, 71))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(RelativeDEM)
        self.label_4.setGeometry(QtCore.QRect(40, 10, 271, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label = QtGui.QLabel(RelativeDEM)
        self.label.setGeometry(QtCore.QRect(40, 66, 101, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(RelativeDEM)
        self.comboBox.setGeometry(QtCore.QRect(160, 70, 311, 20))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.formLayoutWidget = QtGui.QWidget(RelativeDEM)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 110, 441, 91))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.formLayoutWidget_2 = QtGui.QWidget(RelativeDEM)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(30, 10, 441, 41))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.verticalLayoutWidget = QtGui.QWidget(RelativeDEM)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 60, 111, 31))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.retranslateUi(RelativeDEM)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), RelativeDEM.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), RelativeDEM.reject)
        QtCore.QMetaObject.connectSlotsByName(RelativeDEM)

    def retranslateUi(self, RelativeDEM):
        RelativeDEM.setWindowTitle(_translate("RelativeDEM", "RelativeDEM", None))
        self.label_2.setText(_translate("RelativeDEM", "The output files are located in the project folder, the relative DEM is added to the display.", None))
        self.label_4.setText(_translate("RelativeDEM", "Perform the Relative DEM Calculation:", None))
        self.label.setText(_translate("RelativeDEM", "Edited Streams :", None))

