import traceback

from PyQt6.QtWidgets import QMessageBox, QMainWindow

from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.dal.EmployeeDAL import EmployeeDAL
from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.models.Employee import Employee
from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.ui.MainWindowExt import MainWindowExt
from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.ui.MainWindowLoginUI import Ui_MainWindow
from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.ui.MainWindowProductUIExt import MainWindowProductUIExt


class MainWindowLoginUIExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.xuly_dangnhap)
    def xuly_dangnhap(self):
        username=self.lineEditUserName.text()
        password=self.lineEditPassword.text()

        employee_dal = EmployeeDAL()
        employee_dal.connect()
        emp = employee_dal.login(username, password)
        if emp != None:
            try:
                login_infor=Employee(username=username,password=password,name=emp.name,id=emp.id)
                #đóng màn hình đăng nhập
                self.MainWindow.close()
                #kích hoạt màn hình qua lý sp
                mainwindow=QMainWindow()
                self.mainUi=MainWindowExt()
                self.mainUi.setupUi(mainwindow)
                self.mainUi.login_employee=login_infor
                self.mainUi.show_login_information()
                self.mainUi.showWindow()
            except:
                traceback.print_exc()
        else:
            msgBox=QMessageBox()
            msgBox.setText("Đăng nhập thất bại\nVui lòng kiểm tra lại thông tin đăng nhập")
            msgBox.setWindowTitle("Thông báo lỗi")
            msgBox.exec()