# Form implementation generated from reading ui file 'D:\24. Tư duy lập trình\class10k\class10k\course1\o_2024y_10m_25d\Quanly_sanpham\ui\MainWindowProductAdvUI.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 611, 71))
        self.label.setStyleSheet("background-color: rgb(58, 175, 169);\n"
"color: rgb(230, 239, 194);")
        self.label.setObjectName("label")
        self.comboBoxCategory = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBoxCategory.setGeometry(QtCore.QRect(170, 100, 251, 22))
        self.comboBoxCategory.setObjectName("comboBoxCategory")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 160, 611, 381))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidgetProduct = QtWidgets.QTableWidget(parent=self.groupBox)
        self.tableWidgetProduct.setObjectName("tableWidgetProduct")
        self.tableWidgetProduct.setColumnCount(4)
        self.tableWidgetProduct.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tableWidgetProduct)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">QUẢN LÝ DANH MỤC - SẢN PHẨM</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Danh mục sản phẩm:"))
        self.groupBox.setTitle(_translate("MainWindow", "Danh sách sản phẩm"))
        item = self.tableWidgetProduct.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidgetProduct.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "name"))
        item = self.tableWidgetProduct.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "quantity"))
        item = self.tableWidgetProduct.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "up"))
