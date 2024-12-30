import traceback

from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.dal.EmployeeDAL import EmployeeDAL

employee_dal=EmployeeDAL()
employee_dal.connect()
list_emp=employee_dal.get_list_employees()
for emp in list_emp:
    print(emp.id,emp.name,emp.username,emp.password)

#Test give detail inf of any Employee
emp=employee_dal.get_detail_employee_by_id(113)
if emp!=None:
    print("EMP=113 FOUND")
    print(emp.id,emp.name,emp.username,emp.password)
else:
    print("EMP=113 NOT FOUND")

#Test log in successfulness
emp=employee_dal.login("admin","2404")
if emp!=None:
    print("Login successful")
else:
    print("Login failed. Please check your login information and try again.!")
