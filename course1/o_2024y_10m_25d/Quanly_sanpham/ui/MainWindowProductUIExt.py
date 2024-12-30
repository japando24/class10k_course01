import os
import traceback
import webbrowser

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QFileDialog, QMessageBox

from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.io.FileFactory import FileFactory
from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.models.ListProduct import ListProduct
from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.models.Product import Product
from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.ui.MainWindowAboutUIExt import MainWindowAboutUIExt
from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.ui.MainWindowProductUI import Ui_MainWindow


class MainWindowProductUIExt(Ui_MainWindow):
    def __init__(self):
        self.login_employee=None
        # self.database_product=ListProduct.queryData() #minh hoa du lieu mau
        self.database_product = ListProduct()
        self.filefactory=FileFactory()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.statusbar.addWidget(self.labelWelcome)
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.actionGioiThieuPhanMem.triggered.connect(self.xuly_momanhinhgioithieu)
        self.actionThoatPhanMem.triggered.connect(self.MainWindow.close)
        self.actionHuongDanSuDungPhanMem.triggered.connect(self.xuly_mohuongdan)
        self.tableWidgetSanPham.itemSelectionChanged.connect(self.xuly_chon_sanpham)
        self.pushButtonLuuMoi.clicked.connect(self.xuly_luu_sanpham)
        self.actionLuufile.triggered.connect(self.xuly_luufile)
        self.actionDocfile.triggered.connect(self.xuly_docfile)
        self.pushButtonChinhSua.clicked.connect(self.xuly_suasanpham)
        self.pushButtonXoa.clicked.connect(self.xuly_xoasanpham)

    def show_login_information(self):
        login_html_welcome=f"<font color='red'>Xin chao :< /font> {self. login_employee.name}"
        self.labelWelcome.setText(login_html_welcome)
    def xuly_momanhinhgioithieu(self):
        mainwindow = QMainWindow()
        self.aboutUi = MainWindowAboutUIExt()
        self.aboutUi. setupUi(mainwindow)
        self.aboutUi.showWindow()
    def xuly_mohuongdan(self):
        #lấy đường dẫn hiện tại cảu phần mềm
        current_path= os.getcwd()
        file_help=f"{current_path}/../assets/huong_dan_phan_mem.pdf"
        webbrowser.open_new(file_help)
    def hienthi_sanpham_len_qtable(self):
            #xóa dữ liệu cũ
        try:
            self.is_completed=False
            self.tableWidgetSanPham.setRowCount(0)
            for i in range(self.database_product.count()):
                product_i = self.database_product.get_product_by_index(i)
                # add 1 new row to QTableWidget:
                self.tableWidgetSanPham.insertRow(i)
                column_id = QTableWidgetItem(str(product_i.id))
                column_name = QTableWidgetItem(product_i.name)
                column_quantity = QTableWidgetItem(str(product_i.quantity))
                if int(product_i.quantity) < 5:
                    column_quantity.setForeground(Qt.GlobalColor.red)
                    column_quantity.setBackground(Qt.GlobalColor.yellow)
                column_price = QTableWidgetItem(str(product_i.price))
                self.tableWidgetSanPham.setItem(i, 0, column_id)
                self.tableWidgetSanPham.setItem(i, 1, column_name)
                self.tableWidgetSanPham.setItem(i, 2, column_quantity)
                self.tableWidgetSanPham.setItem(i, 3, column_price)
            self.is_completed=True
        except:
            traceback.print_exc()

    def xuly_chon_sanpham(self):
        try:
            if self.is_completed==False:
                return
            #to determine selected row by customer on interface of QTableWidget
            row=self.tableWidgetSanPham.currentRow()
            column_id=self.tableWidgetSanPham.item(row,0)
            column_name=self.tableWidgetSanPham.item(row,1)
            column_quantity=self.tableWidgetSanPham.item(row,2)
            column_price=self.tableWidgetSanPham.item(row,3)
            self.lineEditzMaSanPham.setText(column_id.text())
            self.lineEditTenSanPham.setText(column_name.text())
            self.lineEditSoLuong.setText(column_quantity.text())
            self.lineEditDonGia.setText(column_price.text())
        except:
            traceback.print_exc()
    def xuly_luu_sanpham (self):
        try:
            product_new=Product()
            product_new.id=self.lineEditzMaSanPham.text()
            product_new.name = self.lineEditTenSanPham.text()
            product_new.quantity = int(self.lineEditSoLuong.text())
            product_new.price = float(self.lineEditDonGia.text())
            self.database_product.add_product(product_new)
            self.hienthi_sanpham_len_qtable()
        except:
            traceback.print_exc()
    def xuly_luufile(self):
        try:
            file_filter="Định dạng Json file (*.json);; Tất cả các loại file (*)"
            filename,selected_filter=QFileDialog.getSaveFileName(self.MainWindow,filter=file_filter)
            print("Tên file bạn muốn lưu mới:",filename)
            if filename=="":
                return
            self.filefactory.writeData(filename,self.database_product.products)
            msgBox=QMessageBox()
            msgBox.setText(f"Đã xuất dữ liệu ra định danng Json thành công\n."
                           f"Nơi xuất dữ liệu [{filename}]")
            msgBox.setWindowTitle("Thông báo")
            msgBox.exec()
        except:
            traceback.print_exc()
    def xuly_docfile(self):
        file_filter = "Định dạng Json file (*.json);; Tất cả các loại file (*)"
        filename, selected_filter = QFileDialog.getOpenFileName(self.MainWindow, filter=file_filter)
        if filename == "":
            return
        products=self.filefactory.readData(filename,Product)
        self.database_product.products=products
        self.hienthi_sanpham_len_qtable()
    def xuly_suasanpham(self):
        product=self.database_product.find_product_by_id(self.lineEditzMaSanPham.text())
        if product==None:
            return
        product.name=self.lineEditTenSanPham.text()
        product.quantity=int(self.lineEditSoLuong.text())
        product.price=float(self.lineEditDonGia.text())
        self.hienthi_sanpham_len_qtable()
    def xuly_xoasanpham(self):
        msgBox=QMessageBox(self.MainWindow)
        msgBox.setWindowTitle("Xác nhận xóa!")
        msgBox.setIcon(QMessageBox.Icon.Question)
        msgBox.setText(f"Bạn có chắc chắn muốn xóa sản phảm có mã = [{self.lineEditzMaSanPham.text()}] hay không?")
        buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgBox.setStandardButtons(buttons)
        button=msgBox.exec()
        if button==QMessageBox.StandardButton.Yes:
            self.database_product.remove_product_by_id(self.lineEditzMaSanPham.text())
            self.hienthi_sanpham_len_qtable()


