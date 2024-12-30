import mysql.connector
import pandas as pd


class Connector:
    def __init__(self):
        self.server="localhost"
        self.port=3306
        self.database="csdl_10k"
        self.username="root"
        self.password="@Dnb24042004"
    def connect(self,server=None,port=None,database=None,username=None,password=None):
        if server != None:
            self.server=server
            self.port=port
            self.database=database
            self.username=username
            self.password=password
        self.conn= mysql.connector.connect(
            host=self.server,
            port=self.port,
            database=self.database,
            user=self.username,
            password=self.password
            )
    def query(self,sql,val_input=None):
        cursor=self.conn.cursor()
        cursor.execute(sql,val_input)
        return cursor
    def query_df(self,sql,val_input=None):
        cursor=self.conn.cursor()
        cursor.execute(sql,val_input)
        df=pd.DataFrame(cursor.fetchall())
        if not df.empty:
            df.columns=cursor.column_names
        cursor.close()
        return df



