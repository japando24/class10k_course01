import traceback

from PyQt6.QtWidgets import QMainWindow

from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.ui.MainWindow import Ui_MainWindow
from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.ui.MainWindowDoiMatKhauExt import MainWindowDoiMatKhauExt
from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.ui.MainWindowEmployeeUiExt import MainWindowEmployeeUiExt
from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.ui.MainWindowProductAdvUIExt import MainWindowProductAdvUIExt


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.login_employee = None
        self.mainwindowemployee = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MaiWindow=MainWindow
        self.statusbar.addWidget(self.labelWelcome)
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MaiWindow.show()
    def show_login_information(self):
        login_html_welcome=f"<font color='red'>Xin chao :< /font> {self.login_employee.name}"
        self.labelWelcome.setText(login_html_welcome)
    def setupSignalAndSlot(self):
        self.actionDoiMatKhau.triggered.connect(self.xuly_momanhinh_doimatkhau)
        self.actionEmployee.triggered.connect(self.xuly_momanhinh_quanlyemployee)
        self.actionDanhMucSanPham.triggered.connect(self.xuly_momanhinh_quanlysanpham)
    def xuly_momanhinh_doimatkhau(self):
        self.mainwindowdoimatkhau=QMainWindow()
        self.doimatkhauui=MainWindowDoiMatKhauExt()
        self.doimatkhauui.setupUi(self.mainwindowdoimatkhau)
        self.doimatkhauui.hienthi_thongtin(self.login_employee)
        self.doimatkhauui.showWindow()
    def xuly_momanhinh_quanlyemployee(self):
        try:
            self.mainwindowemployee=QMainWindow()
            self.MaiWindow.close()
            self.quanlyemployeeui=MainWindowEmployeeUiExt()
            self.quanlyemployeeui.setupUi(self.mainwindowemployee)
            self.quanlyemployeeui.showWindow()
        except:
            traceback.print_exc()
    def xuly_momanhinh_quanlysanpham(self):
        self.mainwindowproduct=QMainWindow()
        self.quanlyproductui=MainWindowProductAdvUIExt()
        self.quanlyproductui.setupUi(self.mainwindowproduct)
        self.quanlyproductui.showWindow()
