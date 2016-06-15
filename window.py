# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Sun Jun 12 19:37:43 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.setButton = QtWidgets.QPushButton(self.centralWidget)
        self.setButton.setGeometry(QtCore.QRect(220, 210, 121, 27))
        self.setButton.setObjectName("setButton")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 171, 16))
        self.label.setObjectName("label")
        self.translactionButton = QtWidgets.QPushButton(self.centralWidget)
        self.translactionButton.setGeometry(QtCore.QRect(30, 120, 111, 27))
        self.translactionButton.setObjectName("translactionButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(30, 80, 341, 26))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 20))
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionSelect_file = QtWidgets.QAction(MainWindow)
        self.actionSelect_file.setObjectName("actionSelect_file")
        self.actionAbout_our = QtWidgets.QAction(MainWindow)
        self.actionAbout_our.setObjectName("actionAbout_our")
        self.actionAbout_Progrmas = QtWidgets.QAction(MainWindow)
        self.actionAbout_Progrmas.setObjectName("actionAbout_Progrmas")
        self.actionUser_Guide = QtWidgets.QAction(MainWindow)
        self.actionUser_Guide.setObjectName("actionUser_Guide")
        self.actionHyperion_setting = QtWidgets.QAction(MainWindow)
        self.actionHyperion_setting.setObjectName("actionHyperion_setting")
        self.menuMenu.addAction(self.actionSelect_file)
        self.menuMenu.addAction(self.actionHyperion_setting)
        self.menuAbout.addAction(self.actionAbout_our)
        self.menuAbout.addAction(self.actionAbout_Progrmas)
        self.menuAbout.addAction(self.actionUser_Guide)
        self.menuBar.addAction(self.menuMenu.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.setButton.setText(_translate("MainWindow", "Translate seting"))
        self.label.setText(_translate("MainWindow", "hyperion 1.2 plus"))
        self.translactionButton.setText(_translate("MainWindow", "Translation file"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionSelect_file.setText(_translate("MainWindow", "Select file"))
        self.actionAbout_our.setText(_translate("MainWindow", "About Our Group"))
        self.actionAbout_Progrmas.setText(_translate("MainWindow", "About Progrmas"))
        self.actionUser_Guide.setText(_translate("MainWindow", "User Guide"))
        self.actionHyperion_setting.setText(_translate("MainWindow", "Setting"))

