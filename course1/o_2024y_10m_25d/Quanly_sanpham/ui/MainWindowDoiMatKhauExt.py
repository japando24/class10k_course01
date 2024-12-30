from PyQt6.QtWidgets import QMessageBox

from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.dal.EmployeeDAL import EmployeeDAL
from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.ui.MainWindowDoiMatKhau import Ui_MainWindow


class MainWindowDoiMatKhauExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def hienthi_thongtin(self,emp):
        self.lineEditMaNhanSu.setText(f"{emp.id}")
        self.lineEditTenNhanSu.setText(emp.username)
    def setupSignalAndSlot(self):
        self.pushButtonDoiMatKhau.clicked.connect(self.xuly_doimatkhau)
    def xuly_doimatkhau(self):
        #Step 1: Successfulness log in before => Change password
        username=self.lineEditTenNhanSu.text()
        password=self.lineEditMatKhauCu.text()
        employee_dal = EmployeeDAL()
        employee_dal.connect()
        emp = employee_dal.login(username, password)
        if emp == None:
            msgBox=QMessageBox()
            msgBox.setWindowTitle("Lỗi đổi mật khẩu")
            msgBox.setText("Mật khẩu cũ cung cấp bị sai, hãy kiểm tra lại")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.exec()
        else:
            #Step 2: Check Client side new password and retype new password, they are same

            new_password=self.lineEditMatKhauMoi.text()
            confirm_password=self.lineEditXacNhanMK.text()
            if new_password != confirm_password:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Lỗi đổi mật khẩu")
                msgBox.setText("Mật khẩu mới chưa trùng khớp, vui lòng nhập lại")
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.exec()
            else:
                #Step 3: Change password on server (CSDL)
                id=int(self.lineEditMaNhanSu.text())
                result=employee_dal.doimatkhau(id,new_password)
                if result > 0:
                    msg="Đổi mật khẩu thành công"
                else:
                    msg="Đổi mật khẩu thất bại"
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Thông báo")
                msgBox.setText(msg)
                msgBox.setIcon(QMessageBox.Icon.Information)
                msgBox.exec()

