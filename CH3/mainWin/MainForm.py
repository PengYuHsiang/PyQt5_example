# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        #功能表(manubar)設計
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu_E = QtWidgets.QMenu(self.menubar)
        self.menu_E.setObjectName("menu_E")
        MainWindow.setMenuBar(self.menubar)
        #狀態列(statusbar)設計
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #工具列(toolbar)設計
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        #新增4個Action:開啟(fileOpenAction)、新增(fileNewAction)、關閉(fileCloseAction)和新增視窗(addWinAction)
        self.fileOpenAction = QtWidgets.QAction(MainWindow)
        self.fileOpenAction.setObjectName("fileOpenAction")
        self.fileNewAction = QtWidgets.QAction(MainWindow)
        self.fileNewAction.setObjectName("fileNewAction")
        self.fileCloseAction = QtWidgets.QAction(MainWindow)
        self.fileCloseAction.setObjectName("fileCloseAction")
        self.addWinAction = QtWidgets.QAction(MainWindow)
        self.addWinAction.setObjectName("addWinAction")
        #建立功能表/工具列和Action的關係
        self.menu_F.addAction(self.fileOpenAction)
        self.menu_F.addAction(self.fileNewAction)
        self.menu_F.addAction(self.fileCloseAction)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())
        self.toolBar.addAction(self.addWinAction)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_F.setTitle(_translate("MainWindow", "檔案(&F)"))
        self.menu_E.setTitle(_translate("MainWindow", "編輯(&E)"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.fileOpenAction.setText(_translate("MainWindow", "開啟"))
        self.fileOpenAction.setToolTip(_translate("MainWindow", "開啟"))
        self.fileOpenAction.setShortcut(_translate("MainWindow", "Alt+O"))
        self.fileNewAction.setText(_translate("MainWindow", "新增"))
        self.fileNewAction.setToolTip(_translate("MainWindow", "新增"))
        self.fileNewAction.setShortcut(_translate("MainWindow", "Alt+N"))
        self.fileCloseAction.setText(_translate("MainWindow", "關閉"))
        self.fileCloseAction.setToolTip(_translate("MainWindow", "關閉"))
        self.fileCloseAction.setShortcut(_translate("MainWindow", "Alt+C"))
        self.addWinAction.setText(_translate("MainWindow", "新增視窗"))
        self.addWinAction.setToolTip(_translate("MainWindow", "新增視窗"))

