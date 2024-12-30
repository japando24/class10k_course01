from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.models.Product import Product


class ListProduct:
    def __init__(self):
        self.products=[]
    def add_product(self,p):
        self.products.append(p)
    def print_products(self):
        for p in self.products:
            info=str(p)
            print(info)  #can replace row 8 and 9 by "print(p)"

#Cách 1:
    def filter_products(self,min_price,max_price):
        products_filter=[]
        for product in self.products:
            if product.price>=min_price and product.price<=max_price:
                products_filter.append(product)
        return products_filter
#Cách 2: sử dụng lại hàm ListProduct
    def filter_list_product(self,min_price,max_price):
        lp=ListProduct()
        for product in self.products:
            if product.price>=min_price and product.price<=max_price:
                lp.add_product(product)
        return lp

    def find_product_by_id(self,id):
        size=len(self.products)
        i=0
        while i<size:
            p=self.products[i]
            if p.id==id:
                return p
            i=i+1
        return None
#reomove
    def remove_product_by_id(self,id):
        p=self.find_product_by_id(id)
        if p==None:
            return False #Ko ti thấy, xóa thất bại
        else:
            self.products.remove(p)
            return True #Xóa thành công

    def sort_product_price_asc(self):
        for i in range (len(self.products)):
            for j in range(i+1,len(self.products)):
                pi=self.products[i]
                pj=self.products[j]
                if pi.price > pj.price:
                    self.products[j]=pi
                    self.products[i]=pj

    def sort2_product_price(self):
        for i in range(len(self.products)):
            for j in range(i + 1, len(self.products)):
                pi = self.products[i]
                pj = self.products[j]
                if pi.price < pj.price:
                    self.products[j] = pi
                    self.products[i] = pj
                elif pi.price == pj.price:
                    if pi.quantity > pj.quantity:
                        self.products[j] = pi
                        self.products[i] = pj
#BTVN
#(1) thêm 1 Product có giá trùng nhau
#(2) sắp xếp sản phẩm theo giá giảm dần
#   nếu giá sản phâ bằng nhau
#   thì sắp xếp theo SL tăng dần
    @staticmethod
    def queryData():
        database = ListProduct()
        # thêm 1 Product mới:
        database.add_product(Product("P1", "Áo Ấm", 3, 150))
        # Thêm 1 Product mới:

        p = Product("P2", "Áo Gió", 5, 200)
        database.add_product(p)

        # thêm 1 Product mới:
        database.add_product(Product("P3", "Áo Len", 10, 80))
        database.add_product(Product("P4", "Áo 3 Lỗ", 8, 10))
        database.add_product(Product("P5", "Áo Thun", 2, 70))
        return database
    def count(self):
        return len(self.products)
    def get_product_by_index(self,index):
        return self.products[index]
