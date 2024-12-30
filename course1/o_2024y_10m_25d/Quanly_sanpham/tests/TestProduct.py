from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.models.Product import Product

p1=Product()
print("Thông tin của p1:")
print(p1)

p1.id="P113"
p1.name="Dép Lào"
p1.quantity=2
p1.price=100
print(p1)

p2=Product("P114","Dép Tổ Ong",30,140)
print("Dữ liệu của P2:")
print(p2)

p3=Product("P115","Nón lá")
print("Dữ liệu của p3:")
print(p3)

#ôn lại Alias
p4=p3
#--> lúc này ô nhớ mà p3 đang quản lý, có thêm p4 quản lý
#-->alias: p4 đổi giá trị trong ô nhớ sẽ làm p3 đổi, và ngược lại
p4.quantity=999
print("Quantity của p3=",p3.quantity)
p3.quantity=500
print("Quantity của p4=",p4.quantity)

a=Product(name="Dép Lào")
b=a
c=Product(name="Thuốc Lào")
b=c
b.name="Gió Lào"
#Hỏi a.name bằng bao nhiêu?
print("Tên của a =",a.name)
