from class10k.course1.o_2024y_10m_25d.ManagementCustomer.models.Customer import Customer
from class10k.course1.o_2024y_10m_25d.ManagementCustomer.models.ListCustomer import ListCustomer
from class10k.course1.o_2024y_10m_25d.ManagementCustomer.models.TypeCustomer import TypeCustomer
from class10k.course1.o_2024y_10m_25d.ManagementCustomer.models.TypePhone import TypePhone

customer_database=ListCustomer()
c1=Customer("C1","Obama","obama@gmail.com","0903456789",TypePhone.VIETTEL,28,TypeCustomer.VIP)
customer_database.add_customer(c1)
c2=Customer("C2","Putin","putin@gmail.com","0917654321",TypePhone.MOBIFONE,35,TypeCustomer.POTENTIAL)
customer_database.add_customer(c2)
c3=Customer("C3","Trump","trump@gmail.com","0927123456",TypePhone.VINAPHONE,40,TypeCustomer.NORMAL)
customer_database.add_customer(c3)
c4=Customer("C4","Kim Un","kimun@gmail.com","0933456987",TypePhone.VIETTEL,32,TypeCustomer.NORMAL)
customer_database.add_customer(c4)
c5=Customer("C5","John","john@gmail.com","0943265707",TypePhone.VINAPHONE,20,TypeCustomer.VIP)
customer_database.add_customer(c5)
c6=Customer("C6","Peter","peter@gmail.com","0958472216",TypePhone.MOBIFONE,50,TypeCustomer.POTENTIAL)
customer_database.add_customer(c6)

print("MY COSTUMER LIST")
customer_database.print_customers()

print("-"*30)
print("THỐNG KÊ KHÁCH HÀNG VIP")
filter_vip_customers=customer_database.filter_type_customer(TypeCustomer.VIP)
for c in filter_vip_customers:
    print(c)
print("=> Có",len(filter_vip_customers),"VIP Customers")

print("-"*30)
print("THỐNG KÊ KHÁCH HÀNG THƯỜNG")
filter_normal_customers=customer_database.filter_type_customer(TypeCustomer.NORMAL)
for c in filter_normal_customers:
    print(c)
print("=> Có {0} khách hàng thường".format(len(filter_normal_customers)))

print("-"*30)
filter_age_customers=customer_database.filter_age_customers(29,35)
print("Khách hàng có độ tuổi từ 29-35")
filter_age_customers.print_customers()

print("-"*30)
print("THỐNG KÊ KHÁCH HÀNG XÀI MẠNG VIETTEL")
filter_viettel = customer_database.filter_type_phone_customer(TypePhone.VIETTEL)
filter_viettel.print_customers()


print("-"*30)
print("DS KH xếp theo độ tuổi giảm dần")
customer_database.sort_customers_desc_by_age()
customer_database.print_customers()

print("-"*30)
id="C1"
cust=customer_database.findOne(id)
if cust == None:
    print("Không tim thấy khách hàng có mã =",id)
else:
    print("Tim thấy khách hàng có mã =",id,", Thông tin")
    print(cust)
    print(cust.get_details())
    cust.name="Đông Tà"

print("-"*30)
print("Xuất lại Danh sách khách hàng")
customer_database.print_customers()

print("-"*30)
c8=Customer("C8","Tây Độc","taydoc@gmail.com","081178998",TypePhone.MOBIFONE,50,TypeCustomer.POTENTIAL)
customer_database.update_customer(3,c8)
print("Xuất lại Danh sách khách hàng sau khi chỉnh sửa")
customer_database.print_customers()

print("-"*30)
customer_database.remove_customer_by_index(4)
print("Xuất lại Danh sách khách hàng sau khi xóa")
customer_database.print_customers()
id="C100"
result=customer_database.remove_customer_by_id(id)
if result==True:
    print("Xóa KH có mã {0} thành công".format(id))
    print("Xuất tại DS KH sau khi xóa")
    customer_database.print_customers()
else:
    print("Xóa KH có mã {0} thất bại".format(id))