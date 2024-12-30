from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.ui.MainWindowAboutUI import Ui_MainWindow


class MainWindowAboutUIExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        pass