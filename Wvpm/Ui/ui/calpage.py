# -*- coding: utf-8 -*-
# @Time : 2023/4/12 16:05
# @Author : DanYang
# @File : calpage.py
# @Software : PyCharm
import os
import numpy as np
import sys

import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QGridLayout,
    QLabel, QDialog,
    QHBoxLayout, QGroupBox,
    QRadioButton, QTabWidget, QSizePolicy,
    QTableWidget, QWidget, QPushButton, QFileDialog,
    QAbstractItemView, QTableWidgetItem, QLineEdit,
    QVBoxLayout, QCheckBox
)
import Algorithm
import Plot


class Qt_cal(QDialog):
    def __init__(self, parent=None):
        super(Qt_cal, self).__init__(parent=parent)

        # original palette
        self.originalPalette = QApplication.palette()

        # label
        label = QLabel("Description:\n"
                       "1. Calculation module is used to perform individual\n data queries\n"
                       "2. the plotting module is used to set the plotting\n style\n"
                       "3. the table module supports inputting a large amount\n of data\n"
                       "We wish you a pleasant experience!")

        self.create_top_left_group()
        self.create_top_right_group()
        self.create_bottom_left_group()
        self.creat_fileinput()

        # layout
        top_layout = QHBoxLayout()
        top_layout.addWidget(label)

        main_layout = QGridLayout()
        main_layout.addLayout(top_layout, 0, 0, 1, 2)
        main_layout.addWidget(self.top_left_group, 1, 0)
        main_layout.addWidget(self.top_right_group, 1, 1)
        main_layout.addWidget(self.bottom_left_group, 3, 0, 1, 2)
        main_layout.addLayout(self.file_layout, 2, 0, 1, 2)

        self.setFixedSize(700, 1000)
        self.setLayout(main_layout)
        self.setWindowTitle("Wvpm")

    def cal_answer(self):
        T = float(self.wid1.text())
        p = float(self.wid2.text())
        result = [Algorithm.other(p, T, i) for i in ['v', 'h', 's']]
        answer = "v:{0:.4e}\nh:{1:.3f}\ns:{2:.3f}".format(*result)
        self.screen.setText(answer)

    def create_top_left_group(self):
        self.top_left_group = QGroupBox("Calculation")

        layout = QVBoxLayout()
        self.wid1 = QLineEdit()
        self.wid1.adjustSize()
        layout.addWidget(QLabel("T(K)"))
        layout.addWidget(self.wid1)
        self.wid2 = QLineEdit()
        self.wid2.adjustSize()
        self.check_botton = QPushButton("Calculate")
        self.check_botton.clicked.connect(self.cal_answer)
        self.screen = QLabel("")
        layout.addWidget(QLabel("p(Mpa)"))
        layout.addWidget(self.wid2)
        layout.addWidget(self.screen)
        layout.addWidget(self.check_botton)

        self.top_left_group.setLayout(layout)

    def plot_data(self):
        ifT = self.equal_T.isChecked()
        ifp = self.equal_p.isChecked()
        if_all = self.equal_all.isChecked()
        method = [self.plot_style_2.isChecked(), self.plot_style_1.isChecked(), self.plot_style_3.isChecked()]
        nmethod = np.array(['classic', 'dark_background', 'seaborn'])
        nmethod = nmethod[method]
        Plot.plot_data(self.p, self.T, self.nans, self.ans, if_plot_p=ifp, if_plot_T=ifT, if_plot_all=if_all, method=nmethod)

    def create_top_right_group(self):
        self.top_right_group = QGroupBox("Plot")

        layout = QVBoxLayout()
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        self.equal_T = QCheckBox("Plot isothermal maps")
        self.equal_p = QCheckBox("Plot isobaric diagram")
        self.equal_all = QCheckBox("Mapping water vapor properties")
        layout.addWidget(self.equal_T)
        layout.addWidget(self.equal_p)
        layout.addWidget(self.equal_all)
        self.plot_style_1 = QRadioButton("dark_background")
        self.plot_style_2 = QRadioButton("classic")
        self.plot_style_2.setChecked(True)
        self.plot_style_3 = QRadioButton("seaborn")
        self.plot_button = QPushButton("Plot")
        self.plot_button.clicked.connect(self.plot_data)
        layout2.addWidget(QLabel('Drawing style'))
        layout1.addWidget(self.plot_style_2)
        layout1.addWidget(self.plot_style_1)
        layout1.addWidget(self.plot_style_3)
        layout2.addLayout(layout1)
        layout2.addWidget(self.plot_button)
        layout.addLayout(layout2)

        self.top_right_group.setLayout(layout)

    def create_bottom_left_group(self):
        self.bottom_left_group = QTabWidget()
        self.bottom_left_group.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        tab1 = QWidget()
        self.tablewidget = QTableWidget(500, 3)
        self.tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tab1hbox = QHBoxLayout()
        tab1hbox.addWidget(self.tablewidget)
        tab1.setLayout(tab1hbox)
        self.bottom_left_group.addTab(tab1, "Data")

    def creat_fileinput(self):
        self.file_layout = QHBoxLayout()
        lab1 = QLabel("File Input: (.csv)")
        a1 = QPushButton("Select File")
        a1.clicked.connect(self.select_file)
        lab1.setBuddy(a1)
        self.file_layout.addWidget(lab1)
        self.file_layout.addWidget(a1)

    def select_file(self):
        filename = QFileDialog.getOpenFileName(self, "Select File", os.getcwd(), "CSV Files(*.csv);;ALL Files(*)")
        self.filename = filename[0]
        if self.filename:
            self.show_in_group3()

    def show_in_group3(self):
        df = pd.read_csv(self.filename, encoding='gbk')
        value = df.values
        p = value[:, 0]
        T = value[:, 1]
        self.p = p
        self.T = T
        self.ans = df.columns[2]
        self.nans = [Algorithm.other(i, j, self.ans) for i, j in zip(p, T)]
        df[self.ans] = self.nans
        for line in range(df.shape[0]):
            for row in range(df.shape[1]):
                data = QTableWidgetItem(f"{df.iat[line, row]:.5e}")
                self.tablewidget.setItem(line, row, data)
        self.tablewidget.setColumnCount(row + 1)
        self.tablewidget.setRowCount(line + 1)
        columns = list(df.columns)
        columns.append('')
        self.tablewidget.setHorizontalHeaderLabels(columns)
        self.tablewidget.setFixedSize(self.bottom_left_group.size())
        self.tablewidget.setAlternatingRowColors(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cal = Qt_cal()
    cal.show()
    sys.exit(app.exec_())
