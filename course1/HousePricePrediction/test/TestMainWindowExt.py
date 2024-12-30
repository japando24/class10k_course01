from PyQt6.QtWidgets import QApplication, QMainWindow

from class10k.course1.HousePricePrediction.ui.MainWindowExt import MainWindowExt

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()