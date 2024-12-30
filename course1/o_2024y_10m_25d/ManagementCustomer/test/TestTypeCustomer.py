from class10k.course1.o_2024y_10m_25d.ManagementCustomer.models.TypeCustomer import TypeCustomer

def print_type_customer(tc):
    print(type(tc))
    print(tc1.name)
    print(tc1.value)

tc1=TypeCustomer.VIP
print_type_customer(tc1)
#print(type(tc1))
#print(tc1.name)
#print(tc1.value)

tc2=TypeCustomer.POTENTIAL
print_type_customer(tc2)