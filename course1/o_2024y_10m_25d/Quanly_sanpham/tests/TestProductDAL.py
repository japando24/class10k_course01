from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.dal.ProductDAL import ProductDAL

product_dal=ProductDAL()
product_dal.connect()
products=product_dal.get_list_products()
for p in products:
    print(p)

print("-"*30)
min_price=25
max_price=50
results=product_dal.get_list_products_by_price(min_price,max_price)
print(f"Các sản phẩm có giá từ: {min_price} - {max_price}")
for p in results:
    print(p)

print("-"*30)
cateid=3
results=product_dal.get_list_products_by_category(cateid)
print(f"Các sản phẩm thuộc danh mục",cateid,":")
for p in results:
    print(p)

print("-"*30)
name="ST"
results=product_dal.get_list_products_by_name(name)
print(f"Các sản phẩm có từ khóa",name,":")
for p in results:
    print(p)