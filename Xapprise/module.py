#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
 author: Benjamin Lehman
 website: benjaminlehman.net
 last edit: 21:16 9-27
 
"""
import sys
from PyQt4 import QtGui, QtCore


class Mainframe(QtGui.QMainWindow):
    
    def __init__(self):
        super(Mainframe, self).__init__()
        self.initUI()
        
        
    def initUI(self):
        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QtGui.QAction(QtGui.QIcon('img/window-close.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('center example')    
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Mainframe()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()
