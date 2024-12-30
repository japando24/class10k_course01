from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.models.ListProduct import ListProduct
from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.models.Product import Product

database=ListProduct()
#thêm 1 Product mới:
database.add_product(Product("P1","Áo Ấm",3,150))
#Thêm 1 Product mới:

p=Product("P2","Áo Gió",5,200)
database.add_product(p)

#thêm 1 Product mới:
database.add_product(Product("P3","Áo Len",10,80))
database.add_product(Product("P4","Áo 3 Lỗ",8,10))
database.add_product(Product("P5","Áo Thun",2,70))

print("Danh sách sản phẩm trong cơ sở dữ liệu:")
print("ID\tNAME\tQUANTITY\tUnitPrice")
database.print_products()


min_price=80
max_price=200
print("Danh sách các sản phẩm có giá từ ",min_price,"tới",max_price,":")
result=database.filter_products(min_price,max_price)
for p in result:
    print(p)

min_price = 80
max_price = 150
print("Danh sách các sản phẩm có giá từ ", min_price, "tới", max_price, ":")
result=database.filter_list_product(min_price,max_price)
result.print_products()

id_search="P8080"
p_found=database.find_product_by_id(id_search)
if p_found==None:
    print("Tìm đỏ mắt không thấy sản phẩm nào trong kho có mã  = ",id_search)
else:
    print("Đã tìm thấy sản phẩm trong kho có mã = ",id_search)
    print("Thông tin chi tiết của sản phẩm này là:")
    print(p_found)

id_remove=input("Bạn muốn xóa sản phẩm có mã =")
result=database.remove_product_by_id(id_remove)
if result==False:
    print("Xóa sản phẩm có mã = ",id_remove , " thất bại")
else:
    print("Xóa sản phẩm có mã = ",id_remove, "thành công")
    print("Danh sách sản phẩm sau khi xóa:")
    database.print_products()

print("Danh sách sản phẩm theo đơn giá tăng dần:")
database.sort_product_price_asc()
database.print_products()