# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_Wvpm(object):
    def setupUi(self, Wvpm):
        window_size = (2500, 1500)
        Wvpm.setObjectName("Wvpm")
        Wvpm.setFixedSize(*window_size)

        self.label = QtWidgets.QLabel(Wvpm)
        self.label.setGeometry(QtCore.QRect(0, 0, *window_size))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/stream/image/steam.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Wvpm)
        self.label_2.setGeometry(QtCore.QRect(20, 0, *(i/10 for i in window_size)))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(Wvpm)
        self.pushButton.setGeometry(QtCore.QRect(360, 1250, 300, 100))
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(20)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
                                      "{\n"
                                      "    background: rgb(250, 250, 250);\n"
                                      "    border: 2px solid rgb(200, 200, 200)\n"
                                      "}\n"
                                      "")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/stream/image/title.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")

        self.textEdit = QtWidgets.QTextBrowser(Wvpm)
        self.textEdit.setGeometry(QtCore.QRect(1700, 807, 500, 250))
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setStyleSheet("border: 2px solid rgb(255, 255, 255)")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Wvpm)
        QtCore.QMetaObject.connectSlotsByName(Wvpm)

    def retranslateUi(self, Wvpm):
        _translate = QtCore.QCoreApplication.translate
        Wvpm.setWindowTitle(_translate("Wvpm", "Wvpm"))
        Icon = Wvpm.windowIcon()
        Icon.addPixmap(QtGui.QPixmap(":/stream/image/title.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Wvpm.setWindowIcon(Icon)
        self.label_2.setText(_translate("Form", "author: Dan"))
        self.pushButton.setText(_translate("Form", "Start"))
        self.textEdit.setHtml(_translate("Form",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                         "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                         "type=\"text/css\">\n "
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Roman\'; font-size:15pt; "
                                         "font-weight:600; font-style:normal;\">\n "
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                         "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                         "font-family:\'SimSun\'; font-size:9pt;\">Wvpm</span><span style=\" "
                                         "font-family:\'SimSun\'; font-size:9pt; font-weight:400;\"> is a small "
                                         "software for calculating the enthalpy, entropy, specific volume of water "
                                         "vapor related states</span></p>\n "
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                         "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                         "font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:italic; "
                                         "text-decoration: underline;\">Date of creation: 2023/4/12</span></p>\n "
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                         "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                         "font-family:\'SimSun\'; font-size:9pt; font-weight:400;\">Reference: "
                                         "</span><a href=\"http://www.iapws.org/relguide/IAPWS-95.html\"><span "
                                         "style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; "
                                         "text-decoration: underline; color:#0000ff;\">IAPWS-95,</span></a><a "
                                         "href=\"http://www.coolprop.org/v4/\"><span style=\" font-family:\'SimSun\'; "
                                         "font-size:9pt; font-weight:400; text-decoration: underline; "
                                         "color:#0000ff;\">CoolProp</span></a></p></body></html>"))


import image_rc


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cal = Ui_Wvpm()
    windows = QMainWindow()
    cal.setupUi(windows)
    windows.show()
    sys.exit(app.exec_())