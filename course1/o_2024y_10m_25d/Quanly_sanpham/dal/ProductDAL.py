from class10k.course1.connector.Connector import Connector
from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.models.Product import Product


class ProductDAL(Connector):
    def get_list_products(self):
        sql="select * from product"
        cursor=self.query(sql)
        dataset=cursor.fetchall()
        products=[]
        for record in dataset:
            id=record[0]
            name=record[1]
            quantity=record[2]
            price=record[3]
            cateid=record[4]
            #isdeleted=record[5]
            p=Product(id,name, quantity,price, cateid)
            products.append(p)
        cursor.close()
        return products
    def get_list_products_by_price(self,min_price,max_price):
        sql=(f"""
        select * from product
        where price>={min_price} and price<={max_price} 
        order by price asc
        """)
        cursor=self.query(sql)
        dataset=cursor.fetchall()
        products=[]
        for record in dataset:
            id=record[0]
            name=record[1]
            quantity=record[2]
            price=record[3]
            cateid=record[4]
            #isdeleted=record[5]
            p=Product(id,name, quantity,price, cateid)
            products.append(p)
        cursor.close()
        return products
    def get_list_products_by_category(self,cateid):
        sql=f"""
        select * from product
        where cateid={cateid}
        """
        cursor=self.query(sql)
        dataset=cursor.fetchall()
        products=[]
        for record in dataset:
            id=record[0]
            name=record[1]
            quantity=record[2]
            price=record[3]
            cateid=record[4]
            #isdeleted=record[5]
            p=Product(id,name, quantity,price, cateid)
            products.append(p)
        cursor.close()
        return products
    def get_list_products_by_name(self,keyword):
        sql=f"""
        select * from product
        where name like '%{keyword}%'
        """
        cursor=self.query(sql)
        dataset=cursor.fetchall()
        products=[]
        for record in dataset:
            id=record[0]
            name=record[1]
            quantity=record[2]
            price=record[3]
            cateid=record[4]
            #isdeleted=record[5]
            p=Product(id,name, quantity,price, cateid)
            products.append(p)
        cursor.close()
        return products