import traceback

from class10k.course1.connector.Connector import Connector
from class10k.course1.o_2024y_10m_25d.Quanly_sanpham.models.Employee import Employee


class EmployeeDAL(Connector):
    def get_list_employees(self):
        sql="select * from employee"
        cursor=self.query(sql)
        dataset=cursor.fetchall()
        employees=[]
        for record in dataset:
            id=record[0]
            name=record[1]
            username=record[2]
            password=record[3]
            isdeleted=record[4]
            emp=Employee(id,name,username,password,isdeleted)
            employees.append(emp)
        cursor.close()
        return employees
    def get_detail_employee_by_id(self,id):
        sql=f"select * from employee where id={id}"
        cursor=self.query(sql)
        dataset=cursor.fetchone()
        if dataset != None:
            id, name, username, password,isdeleted = dataset
            emp=Employee(id,name,username,password,isdeleted)
        else:
            emp=None
        cursor.close()
        return emp
    def login(self,username,password):
        sql_login="select * from employee where username=%s and password=%s"
        val_input=(username,password)
        cursor=self.query(sql_login,val_input)
        dataset=cursor.fetchone()
        if dataset != None:
            id, name, username, password,isdeleted = dataset
            emp = Employee(id, name, username, password,isdeleted)
        else:
            emp=None
        cursor.close()
        return emp
    def doimatkhau(self,id,newpassword):
        sql_update="update employee set password=%s where id=%s"
        val_input=(newpassword,id)
        cursor=self.query(sql_update,val_input)
        self.conn.commit() #Confirm change dataset
        return cursor.rowcount #trả về dố dòng bị thay đổi trong CSDL
    def insert_nhanvien(self,emp):
        try:
            sql_insert="insert into employee(name,username,password,isdeleted) values (%s,%s,%s,%s)"
            val_input=(emp.name,emp.username,emp.password,emp.isdeleted)
            cursor = self.query(sql_insert, val_input)
            self.conn.commit()  # Confirm change dataset
            return cursor.rowcount  # trả về dố dòng bị thay đổi trong CSDL
        except:
            traceback.print_exc()
    # def update_nhanvien(self,newemp):
    #     sql_update=f"UPDATE employee SET name = %s, username = %s, password = %s, isdeleted = 0 WHERE id = %d"
    #     val_input=(newemp.id,newemp.name,newemp.username,newemp.password,newemp.isdeleted)
    #     cursor = self.query(sql_update, val_input)
    #     self.conn.commit()
    #     return cursor.rowcount# Confirm change dataset
    def delete_nhanvien(self,id):
        sql_delete="delete from employee where id="+str(id)
        cursor=self.query(sql_delete)
        self.conn.commit()
        return cursor.rowcount
    def duavao_bin(self,id):
        sql_update = "update employee set setisdelete=1 where id=%s"
        val_input = (id,)
        cursor = self.query(sql_update, val_input)
        self.conn.commit()  # Confirm change dataset
        return cursor.rowcount  # trả về dố dòng bị thay đổi trong CSDL
