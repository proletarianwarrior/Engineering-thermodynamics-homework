# -*- coding: utf-8 -*-
# @Time : 2023/4/13 2:51
# @Author : DanYang
# @File : main.py
# @Software : PyCharm
import sys

from home import Ui_Wvpm
from calpage import Qt_cal
from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_Wvpm()
    windows = QMainWindow()
    ui.setupUi(windows)
    windows.show()
    cal = Qt_cal(parent=windows)
    ui.pushButton.clicked.connect(cal.show)
    sys.exit(app.exec_())
