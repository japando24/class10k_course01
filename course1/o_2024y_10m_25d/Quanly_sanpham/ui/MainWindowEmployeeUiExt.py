import traceback

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox

from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.dal.EmployeeDAL import EmployeeDAL
from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.models.Employee import Employee
from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.tests.TestEmployeeDAL import employee_dal
from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.ui.MainWindowEmployeeUi import Ui_MainWindow


class MainWindowEmployeeUiExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.employee_dal = EmployeeDAL()
        self.employee_dal.connect()
        self.hienthi_toanboemplpoyee()
        self.setupSignalandSLot()

    def setupSignalandSLot(self):
        self.tableWidgetNhanVien.itemSelectionChanged.connect(self.xuly_xemchitiet_nhanvien)
        self.pushButtonInsert.clicked.connect(self.xuly_insert_nhanvien)
        # self.pushButtonUpdate.clicked.connect(self.xuly_update_nhanvien)
        self.pushButtonDelete.clicked.connect(self.xuly_delete_nhanvien)
        self.pushButtonBin.clicked.connect(self.xuly_duavaobin_nhanvien)
    def showWindow(self):
        self.MainWindow.show()
    def hienthi_toanboemplpoyee(self):
        self.is_completed=False
        #Step 1: Delecte ole dataset, which are showing interface
        self.tableWidgetNhanVien.setRowCount(0)
        #Step2: Truy vấn toàn bo employee thông qua EmployeeDAL

        self.employees=self.employee_dal.get_list_employees()
        print("nhan viên =",len(self.employees))
        for i in range (len(self.employees)):
            emp=self.employees[i]
            self.tableWidgetNhanVien.insertRow(i)
            column_id=QTableWidgetItem(str(emp.id))
            column_name=QTableWidgetItem(emp.name)
            column_username=QTableWidgetItem(emp.username)
            column_password=QTableWidgetItem(emp.password)
            if emp.isdeleted==0 or emp.isdeleted==None:
                column_trangthai=QTableWidgetItem("Active")
            elif emp.isdeleted == 1:
                column_trangthai = QTableWidgetItem("In bin")
                column_trangthai.setForeground(Qt.GlobalColor.red)
            elif emp.isdeleted == 2:
                column_trangthai = QTableWidgetItem("Permanently Deleted")
                column_trangthai.setForeground(Qt.GlobalColor.darkMagenta)
            self.tableWidgetNhanVien.setItem(i, 0 ,column_id)
            self.tableWidgetNhanVien.setItem(i, 1, column_name)
            self.tableWidgetNhanVien.setItem(i, 2, column_username)
            self.tableWidgetNhanVien.setItem(i, 3, column_password)
            self.tableWidgetNhanVien.setItem(i, 4, column_trangthai)
        self.is_completed = True
    def xuly_xemchitiet_nhanvien(self):
        if self.is_completed==False:
            return
        current_row = self.tableWidgetNhanVien.currentRow()
        column_id = self.tableWidgetNhanVien.item(current_row, 0)
        # print(column_id)
        id = int(column_id.text())
        print("id=", id)
        emp = self.employee_dal.get_detail_employee_by_id(id)
        if emp != None:
            self.lineEditId.setText(str(emp.id))
            self.lineEditName.setText(emp.name)
            self.lineEditUsername.setText(emp.username)
            self.lineEditPassword.setText(emp.password)
            if emp.isdeleted == 1:
                self.checkBoxTrangThai.setChecked(True)
            else:
                self.checkBoxTrangThai.setChecked(False)
    def xuly_insert_nhanvien(self):
        emp=Employee()
        #emp.id=int(self.lineEditID.text())
        emp.name=self.lineEditName.text()
        emp.username=self.lineEditUsername.text()
        emp.password=self.lineEditPassword.text()
        emp.isdeleted=0
        self.employee_dal.connect()
        result=employee_dal.insert_nhanvien(emp)
        print(result)
        if result>0:
            self.hienthi_toanboemplpoyee()

    # def xuly_update_nhanvien(self):
    #     try:
    #         newemp=Employee()
    #         newemp.id = int(self.lineEditId.text())
    #         newemp.name=self.lineEditName.text()
    #         newemp.username = self.lineEditUsername.text()
    #         newemp.password = self.lineEditPassword.text()
    #         newemp.isdeleted = 0
    #         employee_dal = EmployeeDAL()
    #         employee_dal.connect()
    #         result = employee_dal.update_nhanvien(newemp)
    #         if result > 0:
    #             self.hienthi_toanboemplpoyee()
    #     except:
    #         traceback.print_exc()
    def xuly_delete_nhanvien(self):
        try:
            msgBox = QMessageBox(self.MainWindow)
            msgBox.setWindowTitle("Xác nhận xóa!")
            msgBox.setIcon(QMessageBox.Icon.Question)
            msgBox.setText(f"Bạn có chắc chắn muốn xóa nhân viên có mã = [{self.lineEditName.text()}] hay không?")
            buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            msgBox.setStandardButtons(buttons)
            button = msgBox.exec()
            if button == QMessageBox.StandardButton.Yes:
                self.is_completed=False
                id=int(self.lineEditId.text())
                #employee_dal = EmployeeDAL()
                #employee_dal.connect()
                result = self.employee_dal.delete_nhanvien(id)
                if result>0:
                    self.hienthi_toanboemplpoyee()
        except:
            traceback.print_exc()
    def xuly_duavaobin_nhanvien(self):
        id = int(self.lineEditId.text())
        employee_dal = EmployeeDAL()
        employee_dal.connect()
        result = employee_dal.duavao_bin(id)
        if result > 0:
            self.hienthi_toanboemplpoyee()





