# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlg_Editor.ui'
#
# Created: Fri Sep 30 08:49:03 2016
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

class Ui_Editor(object):
    def setupUi(self, Editor):
        Editor.setObjectName(_fromUtf8("Editor"))
        Editor.resize(480, 266)
        Editor.setMinimumSize(QtCore.QSize(372, 266))
        Editor.setMaximumSize(QtCore.QSize(591, 397))
        self.button_box = QtGui.QDialogButtonBox(Editor)
        self.button_box.setGeometry(QtCore.QRect(150, 140, 161, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.formLayoutWidget = QtGui.QWidget(Editor)
        self.formLayoutWidget.setGeometry(QtCore.QRect(130, 100, 212, 21))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)

        self.retranslateUi(Editor)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), Editor.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), Editor.reject)
        QtCore.QMetaObject.connectSlotsByName(Editor)

    def retranslateUi(self, Editor):
        Editor.setWindowTitle(_translate("Editor", "StreamWindow", None))
        self.label_2.setText(_translate("Editor", "Start the editor toolbar for editing streams", None))

