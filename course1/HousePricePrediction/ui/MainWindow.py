# Form implementation generated from reading ui file 'D:\24. Tư duy lập trình\class10k\class10k\course1\HousePricePrediction\ui\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(858, 829)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 551, 41))
        self.label.setStyleSheet("background-color: rgb(13, 124, 102);\n"
"color: rgb(189, 232, 202);")
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 551, 151))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(189, 232, 202);")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditDataset = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditDataset.setGeometry(QtCore.QRect(130, 30, 241, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditDataset.setFont(font)
        self.lineEditDataset.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditDataset.setObjectName("lineEditDataset")
        self.pushButtonChoosedataset = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonChoosedataset.setGeometry(QtCore.QRect(390, 30, 111, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButtonChoosedataset.setFont(font)
        self.pushButtonChoosedataset.setStyleSheet("background-color: rgb(215, 195, 241);")
        self.pushButtonChoosedataset.setObjectName("pushButtonChoosedataset")
        self.lineEditTrainRate = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditTrainRate.setGeometry(QtCore.QRect(130, 70, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditTrainRate.setFont(font)
        self.lineEditTrainRate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditTrainRate.setObjectName("lineEditTrainRate")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(180, 70, 31, 21))
        self.label_4.setObjectName("label_4")
        self.pushButtonTrain = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonTrain.setGeometry(QtCore.QRect(130, 110, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButtonTrain.setFont(font)
        self.pushButtonTrain.setStyleSheet("background-color: rgb(215, 195, 241);")
        self.pushButtonTrain.setObjectName("pushButtonTrain")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 240, 551, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(215, 195, 241);\n"
"background-color: rgb(189, 232, 202);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButtonEvaluate = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButtonEvaluate.setGeometry(QtCore.QRect(30, 70, 91, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButtonEvaluate.setFont(font)
        self.pushButtonEvaluate.setStyleSheet("background-color: rgb(215, 195, 241);")
        self.pushButtonEvaluate.setObjectName("pushButtonEvaluate")
        self.lineEditMAE = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditMAE.setGeometry(QtCore.QRect(220, 40, 241, 22))
        self.lineEditMAE.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditMAE.setText("")
        self.lineEditMAE.setObjectName("lineEditMAE")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(150, 40, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEditMSE = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditMSE.setGeometry(QtCore.QRect(220, 70, 241, 22))
        self.lineEditMSE.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditMSE.setText("")
        self.lineEditMSE.setObjectName("lineEditMSE")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(150, 70, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEditRMSE = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditRMSE.setGeometry(QtCore.QRect(220, 100, 241, 22))
        self.lineEditRMSE.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditRMSE.setText("")
        self.lineEditRMSE.setObjectName("lineEditRMSE")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(150, 100, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 400, 551, 121))
        self.groupBox_3.setStyleSheet("background-color: rgb(189, 232, 202);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButtonSaveModel = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonSaveModel.setGeometry(QtCore.QRect(130, 80, 81, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButtonSaveModel.setFont(font)
        self.pushButtonSaveModel.setStyleSheet("background-color: rgb(215, 195, 241);")
        self.pushButtonSaveModel.setObjectName("pushButtonSaveModel")
        self.pushButtonCreateFile = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonCreateFile.setGeometry(QtCore.QRect(390, 40, 111, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButtonCreateFile.setFont(font)
        self.pushButtonCreateFile.setStyleSheet("background-color: rgb(215, 195, 241);")
        self.pushButtonCreateFile.setObjectName("pushButtonCreateFile")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(30, 40, 81, 16))
        self.label_8.setObjectName("label_8")
        self.lineEditTrainModelName = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.lineEditTrainModelName.setGeometry(QtCore.QRect(130, 40, 241, 22))
        self.lineEditTrainModelName.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditTrainModelName.setObjectName("lineEditTrainModelName")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 540, 831, 241))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("background-color: rgb(65, 179, 162);\n"
"color: rgb(255, 255, 255);")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(30, 40, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.comboBoxTrainModel = QtWidgets.QComboBox(parent=self.groupBox_4)
        self.comboBoxTrainModel.setGeometry(QtCore.QRect(150, 40, 261, 22))
        self.comboBoxTrainModel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBoxTrainModel.setObjectName("comboBoxTrainModel")
        self.pushButtonTaiModel = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.pushButtonTaiModel.setGeometry(QtCore.QRect(440, 40, 91, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButtonTaiModel.setFont(font)
        self.pushButtonTaiModel.setStyleSheet("background-color: rgb(189, 232, 202);\n"
"color: rgb(13, 124, 102);")
        self.pushButtonTaiModel.setObjectName("pushButtonTaiModel")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(30, 90, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEditIncome = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEditIncome.setGeometry(QtCore.QRect(210, 90, 121, 22))
        self.lineEditIncome.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEditIncome.setText("")
        self.lineEditIncome.setObjectName("lineEditIncome")
        self.lineEditHouseAge = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEditHouseAge.setGeometry(QtCore.QRect(210, 130, 121, 22))
        self.lineEditHouseAge.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEditHouseAge.setText("")
        self.lineEditHouseAge.setObjectName("lineEditHouseAge")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(30, 130, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEditRooms = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEditRooms.setGeometry(QtCore.QRect(630, 90, 121, 22))
        self.lineEditRooms.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEditRooms.setText("")
        self.lineEditRooms.setObjectName("lineEditRooms")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(360, 90, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEditBedrooms = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEditBedrooms.setGeometry(QtCore.QRect(630, 130, 121, 22))
        self.lineEditBedrooms.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEditBedrooms.setText("")
        self.lineEditBedrooms.setObjectName("lineEditBedrooms")
        self.label_13 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(360, 130, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEditPopulation = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEditPopulation.setGeometry(QtCore.QRect(210, 170, 121, 22))
        self.lineEditPopulation.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEditPopulation.setText("")
        self.lineEditPopulation.setObjectName("lineEditPopulation")
        self.label_14 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(30, 170, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.pushButtonPredict = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.pushButtonPredict.setGeometry(QtCore.QRect(460, 170, 81, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButtonPredict.setFont(font)
        self.pushButtonPredict.setStyleSheet("background-color: rgb(215, 195, 241);\n"
"color: rgb(0, 0, 0);")
        self.pushButtonPredict.setObjectName("pushButtonPredict")
        self.lineEditHousePrice = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEditHousePrice.setGeometry(QtCore.QRect(670, 170, 151, 22))
        self.lineEditHousePrice.setStyleSheet("background-color: rgb(215, 195, 241);\n"
"color: rgb(0, 0, 0);")
        self.lineEditHousePrice.setText("")
        self.lineEditHousePrice.setObjectName("lineEditHousePrice")
        self.label_15 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(560, 170, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.pushButtonAdvance = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.pushButtonAdvance.setGeometry(QtCore.QRect(360, 170, 81, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButtonAdvance.setFont(font)
        self.pushButtonAdvance.setStyleSheet("background-color: rgb(215, 195, 241);\n"
"color: rgb(0, 0, 0);")
        self.pushButtonAdvance.setObjectName("pushButtonAdvance")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 858, 26))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">DỰ BÁO GIÁ NHÀ</span></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Train mô hình:"))
        self.label_2.setText(_translate("MainWindow", "Dataset:"))
        self.lineEditDataset.setText(_translate("MainWindow", "USA_Housing.csv"))
        self.pushButtonChoosedataset.setText(_translate("MainWindow", "Choose dataset"))
        self.lineEditTrainRate.setText(_translate("MainWindow", "80"))
        self.label_3.setText(_translate("MainWindow", "Tỷ lệ train:"))
        self.label_4.setText(_translate("MainWindow", "%"))
        self.pushButtonTrain.setText(_translate("MainWindow", "Train"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Đánh giá chất lượng mô hình:"))
        self.pushButtonEvaluate.setText(_translate("MainWindow", "Evaluate"))
        self.label_5.setText(_translate("MainWindow", "MAE:"))
        self.label_6.setText(_translate("MainWindow", "MSE:"))
        self.label_7.setText(_translate("MainWindow", "RMSE:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Lưu mô hình để tái sử dụng:"))
        self.pushButtonSaveModel.setText(_translate("MainWindow", "Save model"))
        self.pushButtonCreateFile.setText(_translate("MainWindow", "Create File"))
        self.label_8.setText(_translate("MainWindow", "Nơi lưu:"))
        self.lineEditTrainModelName.setText(_translate("MainWindow", "housingmodel.zip"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Sử dụng mô hình:"))
        self.label_9.setText(_translate("MainWindow", "Chọn mô hình:"))
        self.pushButtonTaiModel.setText(_translate("MainWindow", "Tải Model"))
        self.label_10.setText(_translate("MainWindow", "Avg. Area Income:"))
        self.label_11.setText(_translate("MainWindow", "Avg. Area House Age:"))
        self.label_12.setText(_translate("MainWindow", "Avg. Area Number of Rooms:"))
        self.label_13.setText(_translate("MainWindow", "Avg. Area Number of Bedrooms:"))
        self.label_14.setText(_translate("MainWindow", "Area Population:"))
        self.pushButtonPredict.setText(_translate("MainWindow", "Predict"))
        self.label_15.setText(_translate("MainWindow", "House Price:"))
        self.pushButtonAdvance.setText(_translate("MainWindow", "Advance"))
