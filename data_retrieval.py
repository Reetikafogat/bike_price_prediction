import mysql.connector as mc
conn = mc.connect(
    host='localhost',
    user='root',
    password='reetika',
    database='ml1',
    charset='utf8'
)

cur = conn.cursor() 
query = "select * from Bike"

cur.execute(query) 
for record in cur.fetchall():
    print(record) 

cur.close()
conn.close() 

