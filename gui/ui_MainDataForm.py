# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\AlcheView\gui\MainDataForm.ui'
#
# Created: Sat May 02 15:12:17 2015
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_MainDataWindow(object):
    def setupUi(self, MainDataWindow):
        MainDataWindow.setObjectName(_fromUtf8("MainDataWindow"))
        MainDataWindow.resize(586, 545)
        self.centralwidget = QtGui.QWidget(MainDataWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_ForDataBrowser = QtGui.QVBoxLayout()
        self.verticalLayout_ForDataBrowser.setObjectName(_fromUtf8("verticalLayout_ForDataBrowser"))
        self.verticalLayout.addLayout(self.verticalLayout_ForDataBrowser)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_Refresh = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Refresh.setObjectName(_fromUtf8("pushButton_Refresh"))
        self.horizontalLayout.addWidget(self.pushButton_Refresh)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainDataWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainDataWindow)
        QtCore.QMetaObject.connectSlotsByName(MainDataWindow)

    def retranslateUi(self, MainDataWindow):
        MainDataWindow.setWindowTitle(_translate("MainDataWindow", "MainWindow", None))
        self.pushButton_Refresh.setText(_translate("MainDataWindow", "Обновить", None))

