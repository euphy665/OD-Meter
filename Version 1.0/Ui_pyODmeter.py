# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\OneDrive - 南方科技大学\08 Code\pyEIT_Ying\pyODmeter.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1089, 738)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(150, 77, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.bg = QtWidgets.QPushButton(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(150, 130, 161, 34))
        self.bg.setObjectName("bg")
        self.data = QtWidgets.QPushButton(self.centralwidget)
        self.data.setGeometry(QtCore.QRect(310, 130, 161, 34))
        self.data.setObjectName("data")
        self.single = QtWidgets.QPushButton(self.centralwidget)
        self.single.setGeometry(QtCore.QRect(470, 130, 161, 34))
        self.single.setObjectName("single")
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        self.Save.setGeometry(QtCore.QRect(630, 130, 161, 34))
        self.Save.setObjectName("Save")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(630, 260, 161, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.ODlabel = QtWidgets.QLabel(self.centralwidget)
        self.ODlabel.setGeometry(QtCore.QRect(630, 300, 81, 18))
        self.ODlabel.setObjectName("ODlabel")
        self.gamma12label = QtWidgets.QLabel(self.centralwidget)
        self.gamma12label.setGeometry(QtCore.QRect(630, 390, 81, 18))
        self.gamma12label.setObjectName("gamma12label")
        self.OD = QtWidgets.QLineEdit(self.centralwidget)
        self.OD.setGeometry(QtCore.QRect(630, 320, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.OD.setFont(font)
        self.OD.setObjectName("OD")
        self.gamma12 = QtWidgets.QLineEdit(self.centralwidget)
        self.gamma12.setGeometry(QtCore.QRect(630, 410, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.gamma12.setFont(font)
        self.gamma12.setObjectName("gamma12")
        self.Paras = QtWidgets.QLabel(self.centralwidget)
        self.Paras.setGeometry(QtCore.QRect(150, 479, 513, 18))
        self.Paras.setObjectName("Paras")
        self.Paraname = QtWidgets.QLabel(self.centralwidget)
        self.Paraname.setGeometry(QtCore.QRect(150, 500, 641, 18))
        self.Paraname.setObjectName("Paraname")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 550, 641, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Offset_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Offset_2.setObjectName("Offset_2")
        self.horizontalLayout_2.addWidget(self.Offset_2)
        self.Amplitude_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Amplitude_2.setObjectName("Amplitude_2")
        self.horizontalLayout_2.addWidget(self.Amplitude_2)
        self.OD_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.OD_2.setObjectName("OD_2")
        self.horizontalLayout_2.addWidget(self.OD_2)
        self.Delta_p_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Delta_p_2.setObjectName("Delta_p_2")
        self.horizontalLayout_2.addWidget(self.Delta_p_2)
        self.gamma12_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.gamma12_2.setObjectName("gamma12_2")
        self.horizontalLayout_2.addWidget(self.gamma12_2)
        self.Omega_c_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Omega_c_2.setObjectName("Omega_c_2")
        self.horizontalLayout_2.addWidget(self.Omega_c_2)
        self.Delta_c_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Delta_c_2.setObjectName("Delta_c_2")
        self.horizontalLayout_2.addWidget(self.Delta_c_2)
        self.fileDirectory = QtWidgets.QLineEdit(self.centralwidget)
        self.fileDirectory.setGeometry(QtCore.QRect(250, 610, 361, 31))
        self.fileDirectory.setObjectName("fileDirectory")
        self.fileDirectory_2 = QtWidgets.QLabel(self.centralwidget)
        self.fileDirectory_2.setGeometry(QtCore.QRect(150, 585, 651, 18))
        self.fileDirectory_2.setObjectName("fileDirectory_2")
        self.enableFitting = QtWidgets.QCheckBox(self.centralwidget)
        self.enableFitting.setGeometry(QtCore.QRect(630, 220, 161, 22))
        self.enableFitting.setObjectName("enableFitting")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(150, 520, 641, 27))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Offset = QtWidgets.QLineEdit(self.layoutWidget1)
        self.Offset.setObjectName("Offset")
        self.horizontalLayout.addWidget(self.Offset)
        self.Amplitude = QtWidgets.QLineEdit(self.layoutWidget1)
        self.Amplitude.setObjectName("Amplitude")
        self.horizontalLayout.addWidget(self.Amplitude)
        self.OD_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.OD_3.setObjectName("OD_3")
        self.horizontalLayout.addWidget(self.OD_3)
        self.Delta_p = QtWidgets.QLineEdit(self.layoutWidget1)
        self.Delta_p.setObjectName("Delta_p")
        self.horizontalLayout.addWidget(self.Delta_p)
        self.gamma_12 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.gamma_12.setObjectName("gamma_12")
        self.horizontalLayout.addWidget(self.gamma_12)
        self.Omega_c = QtWidgets.QLineEdit(self.layoutWidget1)
        self.Omega_c.setObjectName("Omega_c")
        self.horizontalLayout.addWidget(self.Omega_c)
        self.Delta_c = QtWidgets.QLineEdit(self.layoutWidget1)
        self.Delta_c.setObjectName("Delta_c")
        self.horizontalLayout.addWidget(self.Delta_c)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 220, 471, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.graph_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.graph_layout.setContentsMargins(0, 0, 0, 0)
        self.graph_layout.setObjectName("graph_layout")
        self.STOP = QtWidgets.QPushButton(self.centralwidget)
        self.STOP.setGeometry(QtCore.QRect(310, 165, 161, 34))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.STOP.setFont(font)
        self.STOP.setObjectName("STOP")
        self.fileName = QtWidgets.QLineEdit(self.centralwidget)
        self.fileName.setGeometry(QtCore.QRect(620, 610, 81, 31))
        self.fileName.setObjectName("fileName")
        self.autoIndex = QtWidgets.QCheckBox(self.centralwidget)
        self.autoIndex.setGeometry(QtCore.QRect(180, 612, 31, 21))
        self.autoIndex.setText("")
        self.autoIndex.setObjectName("autoIndex")
        self.fileIndex = QtWidgets.QLineEdit(self.centralwidget)
        self.fileIndex.setGeometry(QtCore.QRect(710, 610, 81, 31))
        self.fileIndex.setObjectName("fileIndex")
        self.saveStatus = QtWidgets.QLineEdit(self.centralwidget)
        self.saveStatus.setGeometry(QtCore.QRect(150, 650, 641, 31))
        self.saveStatus.setObjectName("saveStatus")
        self.clearBg = QtWidgets.QPushButton(self.centralwidget)
        self.clearBg.setGeometry(QtCore.QRect(150, 165, 161, 34))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.clearBg.setFont(font)
        self.clearBg.setObjectName("clearBg")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1089, 30))
        self.menubar.setObjectName("menubar")
        self.menupy = QtWidgets.QMenu(self.menubar)
        self.menupy.setObjectName("menupy")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menupy.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "OD METER Ying ver.1.0"))
        self.bg.setText(_translate("MainWindow", "Take Background"))
        self.data.setText(_translate("MainWindow", "Take Data"))
        self.single.setText(_translate("MainWindow", "Single Frame"))
        self.Save.setText(_translate("MainWindow", "Save Data"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Two-level"))
        self.comboBox.setItemText(1, _translate("MainWindow", "EIT"))
        self.ODlabel.setText(_translate("MainWindow", "OD"))
        self.gamma12label.setText(_translate("MainWindow", "gamma12"))
        self.OD.setText(_translate("MainWindow", "200"))
        self.gamma12.setText(_translate("MainWindow", "0.0001"))
        self.Paras.setText(_translate("MainWindow", "Initial fitting parameters & Real-time fitting parameters"))
        self.Paraname.setText(_translate("MainWindow", "Offset    Amplitude  OD        Delta_p   gamma12    Omega_c   Delta_c"))
        self.fileDirectory_2.setText(_translate("MainWindow", "Auto-index File Directory                         Name/Prefix From"))
        self.enableFitting.setText(_translate("MainWindow", "Enable Fitting"))
        self.STOP.setText(_translate("MainWindow", "STOP"))
        self.clearBg.setText(_translate("MainWindow", "Clear Background"))
        self.menupy.setTitle(_translate("MainWindow", "OD"))