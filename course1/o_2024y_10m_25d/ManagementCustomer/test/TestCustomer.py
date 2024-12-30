from class10k.course1.o_2024y_10m_25d.ManagementCustomer.models.Customer import Customer
from class10k.course1.o_2024y_10m_25d.ManagementCustomer.models.TypeCustomer import TypeCustomer

#Way 1:
c1=Customer("C1","Obama","obama@gmail.com","0123456789",28,TypeCustomer.VIP)
print(c1)

#Way 2:
c2=Customer()
c2.id="C2"
c2.name="Putin"
c2.email="putin@gmail.com"
c2.phone="0906548796"
c2.age=35
c2.tc=TypeCustomer.POTENTIAL
print(c2)