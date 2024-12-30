from class10k.course1.connector.Connector import Connector
from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.models.Category import Category


class CategoryDAL(Connector):
    def get_list_categories(self):
        sql="select * from category"
        cursor=self.query(sql)
        dataset=cursor.fetchall()
        categories=[]
        for record in dataset:
            id=record[0]
            name=record[1]
            isdeleted=record[2]
            cate=Category(id,name,isdeleted)
            categories.append(cate)
        cursor.close()
        return categories