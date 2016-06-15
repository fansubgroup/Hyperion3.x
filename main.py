#!/usr/bin/python3
# -*- coding: utf-8 -*-
from window import Ui_MainWindow as Ui_mainWin
from setting2 import Ui_DockWidget as Ui_settingWin
from edit2 import Ui_Form as Ui_editWin
import core
import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox

class editWin(QtWidgets.QDockWidget, Ui_editWin):
    def __init__(self):
        super(editWin,self).__init__()
        self.setupUi(self)
        if os.path.isfile("README"):
            showhelp = open("README").read()
            self.showEdit.setText(showhelp)

class settingWin(QtWidgets.QDockWidget, Ui_settingWin):
    def __init__(self):
        super(settingWin,self).__init__()
        self.setupUi(self)
        if os.path.exists("hyperion.conf"):
            get_conf = open("hyperion.conf", "r")
            self.value_1 = get_conf.readline()
            self.value_2 = get_conf.readline()
            get_conf.close()
            if len(self.value_1) != 0 and len(self.value_2) != 0:
                self.lineEdit.setText(self.value_1)
                self.lineEdit_2.setText(self.value_2)
            else:
                self.lineEdit.setText("en")
                self.lineEdit_2.setText("ch")
        else:
            create_file = open("hyperion.conf", "a")
            create_file.close()
            self.lineEdit.setText("en")
            self.lineEdit_2.setText("ch")

        if os.path.exists("app.conf"):
            get_app = open("app.conf", "r")
            self.value_4 = get_app.readline()
            self.value_5 = get_app.readline()
            get_app.close()
            if len(self.value_5) != 0 and len(self.value_4) != 0:
                self.lineEdit_4.setText(self.value_4)
                self.lineEdit_5.setText(self.value_5)
        else:
            create_file= open("app.conf", "a")
            create_file.close()
            
        self.applyButton.clicked.connect(self.ApplyChange)
        self.cancelButton.clicked.connect(self.close)
        self.selectButton.clicked.connect(self.SaveFile)

    def ApplyChange(self):
        self.src = self.lineEdit.text()
        self.dst = self.lineEdit_2.text()
        
        self.save_file_path = self.lineEdit_3.text()
        
        self.appid = self.lineEdit_4.text()
        self.skey = self.lineEdit_5.text()
        
        if os.path.exists("hyperion.conf"):
            os.remove("hyperion.conf")
            
        if os.path.exists("app.conf"):
           os.remove("app.conf")
        
        if len(self.src) != 0 and len(self.dst) != 0:
            save_hy = open("hyperion.conf", "a")
            save_hy.writelines(self.src)
            save_hy.writelines(self.dst)
            save_hy.close()
        else:
            QMessageBox.warning(self, "Oops", "Maybe you should first enter a src and dst")
        
        if len(self.appid) != 0 and len(self.skey) != 0:
            save_app = open("app.conf", "a")
            save_app.writelines(self.appid)
            save_app.writelines(self.skey)
            save_app.close()
        else:
            QMessageBox.warning(self, "Oops", "Maybe you should first enter a appid and skey")
            
        if len(self.save_file_path) == 0:
            self.save_file_path = os.path.abspath(".")
            
        save_path_fp = open("hyperion.conf", "a")
        save_path_fp.writelines(self.save_file_path)
        save_path_fp.close()

    def SaveFile(self):
            dirname = QFileDialog.getExistingDirectory(self, "Open file to save")
            if dirname:
                self.lineEdit_3.setText(dirname)
            else:
                QMessageBox.warning(self, "Oops", "There is some error with open file name")

class mainWin(QtWidgets.QMainWindow, Ui_mainWin):
    def __init__(self, parent = None):
        super(mainWin,self).__init__(parent)
        self.setupUi(self)
        
        cat = open("hyperion.conf", "a")
        cat.close()
        
        dog = open("app.conf", "a")
        dog.close()
        
        self.translactionButton.clicked.connect(self.Translation)
        self.actionSelect_file.triggered.connect(self.BrowseFile)
        self.setButton.clicked.connect(self.ShowSetting)
        self.actionHyperion_setting.triggered.connect(self.ShowSetting)
        self.actionAbout_our.triggered.connect(self.ShowOur)
        self.actionAbout_Progrmas.triggered.connect(self.ShowPro)
        self.actionUser_Guide.triggered.connect(self.ShowEdit)
        
    def ShowEdit(self):
        self.Show = editWin()
        self.Show.show()
    
    def ShowOur(self):
        QMessageBox.information(self, "About Our Group", "Our group name is fansubgroup, and you can follow us at github https://github.com/fansubgroup.")
        
    def ShowPro(self):
        QMessageBox.information(self, "About Progrmas", " We are working to reduce the pressure on the subtitles group to help translate simple sentences")
        
    def ShowSetting(self):
        self.Show = settingWin()
        self.Show.show()
    
    def Translation(self):
        if len(self.lineEdit.text()) != 0:
            self.open_path=self.lineEdit.text()
                
            if os.path.exists(self.open_path):
                if core.main(self.open_path):
                    QMessageBox.warning(self, "Oops", "Faild to translate")
                else:
                    QMessageBox.information(self, "Successful", "Translate done")
            else:
                QMessageBox.warning(self,"Oops","Please set you Language")
        else:
            QMessageBox.warning(self, "Oops","Please choice a srt file")
        
        
    def BrowseFile(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "Open File", ".", "SRT FILE (*.srt);;All Files (*)")
        if filename:
            self.lineEdit.setText(filename)


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = mainWin()
    main.show()
    sys.exit(app.exec_())
