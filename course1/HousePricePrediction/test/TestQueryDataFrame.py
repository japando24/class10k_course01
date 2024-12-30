from class10k.course1.connector.Connector import Connector

connector=Connector()
connector.connect()
df=connector.query_df("select * from usa_housing")
print(df)