# -*- coding: utf-8 -*-

"""
Created on Wed Mar 20 10:12:03 2013

@author: Vyakhorev, Dozdikov
"""

if __name__ == "__main__":
    from gui_main import *
    reload(sys)
    sys.setdefaultencoding('utf-8')
    app = QtGui.QApplication(sys.argv)
    #Start interacting with user
    form = gui_MainWindow(app)
    form.show()
    app.exec_()