from PyQt6.QtWidgets import QTableWidgetItem

from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.dal.CategoryDAL import CategoryDAL
from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.dal.ProductDAL import ProductDAL
from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.ui.MainWindowProductAdvUI import Ui_MainWindow


class MainWindowProductAdvUIExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.hienthi_danhsachdanhmuc_combobox()
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def hienthi_danhsachdanhmuc_combobox(self):
        cate_dal = CategoryDAL()
        cate_dal.connect()
        list_cate = cate_dal.get_list_categories()
        for cate in list_cate:
            self.comboBoxCategory.addItem(str(cate),cate)
    def setupSignalAndSlot(self):
        self.comboBoxCategory.activated.connect(self.xuly_hienthi_sanpham_theodanhmuc)
    def xuly_hienthi_sanpham_theodanhmuc(self):
        #Cần phải lấy được category nào đang được chọn trên combobox
        cate=self.comboBoxCategory.currentData()
        print("Danh mục bạn chọn để xem sản phẩm:",cate.id)
        product_dal = ProductDAL()
        product_dal.connect()
        cateid = cate.id
        results = product_dal.get_list_products_by_category(cateid)
        print(f"Các sản phẩm thuộc danh mục", cateid, ":")
        self.tableWidgetProduct.setRowCount(0)
        i=0
        for p in results:
            print(p)
            self.tableWidgetProduct.insertRow(i)
            column_id = QTableWidgetItem(str(p.id))
            column_name = QTableWidgetItem(p.name)
            column_quantity = QTableWidgetItem(p.quantity)
            column_price = QTableWidgetItem(str(p.price))

            self.tableWidgetProduct.setItem(i, 0, column_id)
            self.tableWidgetProduct.setItem(i, 1, column_name)
            self.tableWidgetProduct.setItem(i, 2, column_quantity)
            self.tableWidgetProduct.setItem(i, 3, column_price)

            i=i+1