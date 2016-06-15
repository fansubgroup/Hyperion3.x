# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit2.ui'
#
# Created: Tue Jun 14 20:37:37 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(496, 491)
        self.showEdit = QtWidgets.QTextEdit(Form)
        self.showEdit.setGeometry(QtCore.QRect(0, 0, 491, 491))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showEdit.sizePolicy().hasHeightForWidth())
        self.showEdit.setSizePolicy(sizePolicy)
        self.showEdit.setReadOnly(True)
        self.showEdit.setObjectName("showEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

