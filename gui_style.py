# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

class c_stylish(object):
    # Наследуем отсюда наш QTextBrowser
    def apply_style(self):
        # YOUR CODE HERE
        self.setStyleSheet("background-color: #AAAAAA;")