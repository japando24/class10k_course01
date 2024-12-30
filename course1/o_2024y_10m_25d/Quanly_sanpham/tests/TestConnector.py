import traceback

from class10k.course1.connector.Connector import Connector
try:
    myconnector=Connector()
    myconnector.connect() #ko truyền đối số nào cả -> tức là lấy thông số kết nối mặc định
    cursor=myconnector.conn.cursor()
    sql="select * from employee"
    cursor.execute(sql)
    dataset_employee=cursor.fetchall() #đọc toàn bộ dữ liệu Employee
    for record in dataset_employee:
        id=record[0]
        name=record[1]
        print(id,name)
    cursor.close()
except:
    traceback.print_exc()

# truy vấn thông tin chi tiết của Employee khi biết id:
sql="select * from employee where id=1"
cursor2=myconnector.query(sql)
dataset2=cursor2.fetchone()
if dataset2 != None:
    id,name,username,password=dataset2
    print("name=",name)
    print("password",password)
cursor2.close()

    #minh họa đăng nhập hệ thống:
sql_login="select * from employee where username=%s and password=%s"
val_input=("admin5","123")
cursor_login=myconnector.conn.cursor()
cursor_login.execute(sql_login,val_input)
dataset_login=cursor_login.fetchone()
if dataset_login != None:
    id,name,username,password = dataset_login
    print("name=",name)
    print("password",password)
else:
    print("Fail log in!")
