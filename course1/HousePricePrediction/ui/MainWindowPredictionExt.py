import os
import pickle

import pandas as pd
from PyQt6.QtWidgets import QTableWidgetItem

from class10k.course1.HousePricePrediction.ui.MainWindowPrediction import Ui_MainWindow


class MainWindowPredictionExt(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def showWindow(self):
        self.MainWindow.show()
    def loadAllDataIntoQTable(self):
        self.path = os.getcwd()
        self.path = self.path.replace("test", "dataset\\USA_Housing.csv")
        df = pd.read_csv(self.path)
        modelname="../trained_models/nevergiveup.zip"
        self.trainedmodel = pickle.load(open(modelname, 'rb'))


        self.tableWidgetHouse.setRowCount(0)
        row=0
        for item in df.iloc:
            arr=item.values.tolist()
            self.tableWidgetHouse.insertRow(row)
            j=0
            for cell_value in arr:
                self.tableWidgetHouse.setItem(row,j,QTableWidgetItem(str(cell_value)))
                j=j+1
                if j>=6:
                    input1 = [arr[0], arr[1], arr[2],arr[3], arr[4]]
                    print(input1)
                    prediction1 = self.trainedmodel.predict([input1])
                    print("Housing Price Prediction 1=", prediction1)
                    predicted_price = prediction1[0]
                    self.tableWidgetHouse.setItem(row,j,QTableWidgetItem(str(predicted_price)))
                    break
            row=row+1

        #self.tableWidgetHouse.resizeColumnToContents(10)
