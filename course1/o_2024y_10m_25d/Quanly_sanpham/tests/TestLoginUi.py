import traceback

from PyQt6.QtWidgets import QApplication, QMainWindow

from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.ui.MainWindowLoginUIExt import MainWindowLoginUIExt
try:
    app=QApplication([])
    mainwindow=QMainWindow()
    myui=MainWindowLoginUIExt()
    myui.setupUi(mainwindow)
    myui.showWindow()
    app.exec()
except:
    traceback.print_exc()