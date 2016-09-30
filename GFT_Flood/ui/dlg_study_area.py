# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlg_study_area.ui'
#
# Created: Fri Sep 30 11:34:43 2016
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

class Ui_ClipMultipleLayers(object):
    def setupUi(self, ClipMultipleLayers):
        ClipMultipleLayers.setObjectName(_fromUtf8("ClipMultipleLayers"))
        ClipMultipleLayers.resize(372, 266)
        ClipMultipleLayers.setMinimumSize(QtCore.QSize(372, 266))
        ClipMultipleLayers.setMaximumSize(QtCore.QSize(589, 392))
        self.button_box = QtGui.QDialogButtonBox(ClipMultipleLayers)
        self.button_box.setGeometry(QtCore.QRect(180, 220, 161, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.label_2 = QtGui.QLabel(ClipMultipleLayers)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 341, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(ClipMultipleLayers)
        self.label_4.setGeometry(QtCore.QRect(40, 10, 271, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label = QtGui.QLabel(ClipMultipleLayers)
        self.label.setGeometry(QtCore.QRect(40, 70, 51, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(ClipMultipleLayers)
        self.comboBox.setGeometry(QtCore.QRect(100, 70, 211, 20))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.formLayoutWidget = QtGui.QWidget(ClipMultipleLayers)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 110, 331, 111))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.formLayoutWidget_2 = QtGui.QWidget(ClipMultipleLayers)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(30, 10, 291, 41))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.verticalLayoutWidget = QtGui.QWidget(ClipMultipleLayers)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 60, 61, 31))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.retranslateUi(ClipMultipleLayers)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), ClipMultipleLayers.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), ClipMultipleLayers.reject)
        QtCore.QMetaObject.connectSlotsByName(ClipMultipleLayers)

    def retranslateUi(self, ClipMultipleLayers):
        ClipMultipleLayers.setWindowTitle(_translate("ClipMultipleLayers", "CreateStudyArea", None))
        self.label_2.setText(_translate("ClipMultipleLayers", "The output folder is created in the current project folder.", None))
        self.label_4.setText(_translate("ClipMultipleLayers", "Clip all display layer with the selection layer :", None))
        self.label.setText(_translate("ClipMultipleLayers", "selection :", None))

