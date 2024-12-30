from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.dal.CategoryDAL import CategoryDAL

cate_dal=CategoryDAL()
cate_dal.connect()
list_cate=cate_dal.get_list_categories()
for cate in list_cate:
    print(cate.id,cate.name,cate.isdelete)