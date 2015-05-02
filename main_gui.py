# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
import datetime

from gui.ui_MainDataForm import Ui_MainDataWindow

import db_main
import gui_interm

class gui_MainWindow(QtGui.QMainWindow,Ui_MainDataWindow):

    def __init__(self, app, parent=None):
        super(gui_MainWindow, self).__init__(parent)
        self.app = app
        self.setupUi(self)
        # Эксперимент со ссылками
        self.textBrowser_DataView = gui_LinkedBrowser(self)
        self.verticalLayout_ForDataBrowser.addWidget(self.textBrowser_DataView)
        self.textBrowser_DataView.setOpenLinks(False)

        self.record_list_intm = gui_interm.c_RecordList_intm([db_main.c_EventRecord, db_main.c_NewsRecord])
        self.textBrowser_DataView.set_intm(self.record_list_intm)



class gui_LinkedBrowser(QtGui.QTextBrowser):

    def set_intm(self,intm):
        self.the_interm = intm
        self.setHtml(intm.build_HTML())
        self.anchorClicked.connect(self.print_url)
        self.anchorClicked.connect(self.parse_url)

    def print_url(self,some_url):
        print some_url.toString()

    def parse_url(self,some_url):
        obj = self.the_interm.parse_url(str(some_url.toString()))
        print(str(obj))
        #emit..

    def setSource(self, some_url):
        print some_url

    def print_record(self,obj):

        print str(obj)