import os
import pickle

import numpy as np
import pandas as pd
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QMainWindow
from _testcapi import object_str
from pandas import Index
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from class10k.course1.HousePricePrediction.ui.MainWindow import Ui_MainWindow
from class10k.course1.HousePricePrediction.ui.MainWindowPredictionExt import MainWindowPredictionExt


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.path=os.getcwd()
        self.path=self.path.replace("test","dataset\\USA_Housing.csv")
        self.train_rate=80
        self.test_rate=20
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.lineEditDataset.setText(self.path)
        self.loadTrainedModels()

        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonChoosedataset.clicked.connect(self.chooseDataset)
        self.pushButtonTrain.clicked.connect(self.train_model)
        self.pushButtonEvaluate.clicked.connect((self.evaluate_model))
        self.pushButtonSaveModel.clicked.connect((self.save_model))
        self.pushButtonTaiModel.clicked.connect(self.load_model)
        self.pushButtonPredict.clicked.connect(self.use_model)
        self.pushButtonAdvance.clicked.connect(self.open_detail)
    def chooseDataset(self):
        filters="dataset (*.csv);; Tất cả các loại file (*)"
        filename,selected_filter=QFileDialog.getOpenFileName(self.MainWindow,filter=filters)
        if filename=="":
            return
        self.path=filename
        self.lineEditDataset.setText(self.path) #lineEditDataset
    def train_model(self):
        self.train_rate=int(self.lineEditTrainRate.text())
        self.test_rate=100-self.train_rate

        df = pd.read_csv(self.path)
        X = df[df.columns[:5]]
        y = df['Price']
        # Printing for observation:
        print(X)
        print(y)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=self.test_rate/100, random_state=101)
        """X_train và y_train là để cho mt train
        x_test và y_test là để thử"""

        self.lm = LinearRegression()
        self.lm.fit(self.X_train, self.y_train)

        self.msg=QMessageBox()
        self.msg.setText("Đã train mô hình máy học thành công")
        self.msg.setWindowTitle("Thông báo")
        self.msg.show()
    def evaluate_model(self):
        predictions=self.lm.predict(self.X_test)
        MAE=metrics.mean_absolute_error(self.y_test, predictions)
        MSE=metrics.mean_squared_error(self.y_test, predictions)
        RMSE=np.sqrt(metrics.mean_squared_error(self.y_test, predictions))
        self.lineEditMAE.setText(f"{MAE}")
        self.lineEditMSE.setText(f"{MSE}")
        self.lineEditRMSE.setText(f"{RMSE}")
    def save_model(self):
        try:
            modelname = self.lineEditTrainModelName.text()
            path=f"../trained_models/{modelname}"
            pickle.dump(self.lm, open(path, 'wb'))
            self.msg = QMessageBox()
            self.msg.setText(f"Đã lưu mô hình máy học thành công.\n{path}")
            self.msg.setWindowTitle("Thông báo")
            self.msg.show()
        except:
            self.msg = QMessageBox()
            self.msg.setText(f"Lưu thất bại ...")
            self.msg.setWindowTitle("Thông báo")
            self.msg.setIcon(QMessageBox.Icon.Critical)
            self.msg.show()

    def loadTrainedModels(self):
        path=f"../trained_models/"
        import glob

        txtfiles = []
        for file in glob.glob(f"{path}*.zip"):
            txtfiles.append(file)
        print(txtfiles)
        self.comboBoxTrainModel.addItems(txtfiles)
    def load_model(self):
        selected_trainedmodel=self.comboBoxTrainModel.currentText()
        modelname = selected_trainedmodel

        # Load Trained Machine Learning Model
        self.trainedmodel = pickle.load(open(modelname, 'rb'))

        features = Index(['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
                          'Avg. Area Number of Bedrooms', 'Area Population'],
                         dtype='object')
        # Check coeff again if you want (no need)
        coeff_df = pd.DataFrame(self.trainedmodel.coef_, features, columns=['Coefficient'])
        print(coeff_df)
        self.msg = QMessageBox()
        self.msg.setText(f"Đã tải mô hình máy học thành công")
        self.msg.setWindowTitle("Thông báo")
        self.msg.show()

    def use_model(self):
        print("Input 1:")
        Avg_Area_Income=float(self.lineEditIncome.text())
        Avg_Area_House_Age=float(self.lineEditHouseAge.text())
        Avg_Area_Number_of_Rooms=float(self.lineEditRooms.text())
        Avg_Area_Number_of_Bedrooms=float(self.lineEditBedrooms.text())
        Area_Population=float(self.lineEditPopulation.text())

        input1 = [Avg_Area_Income, Avg_Area_House_Age, Avg_Area_Number_of_Rooms, Avg_Area_Number_of_Bedrooms, Area_Population]
        print(input1)
        prediction1 = self.trainedmodel.predict([input1])
        print("Housing Price Prediction 1=", prediction1)
        price=prediction1[0]
        self.lineEditHousePrice.setText(f"{price}")
    def open_detail(self):
        self.mainwindow = QMainWindow()
        self.myui = MainWindowPredictionExt()
        self.myui.setupUi(self.mainwindow)
        self.myui.loadAllDataIntoQTable()
        self.myui.showWindow()





