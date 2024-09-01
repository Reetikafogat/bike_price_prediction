import mysql.connector as mc

# Connect to MySQL database
conn = mc.connect(
    host='localhost',
    user='root',
    password='reetika',
    database='ml1',
    charset='utf8' 
)

query_to_create_table = """
CREATE TABLE IF NOT EXISTS Bike (
    owner INT,
    brand VARCHAR(40),
    kms_driven INT,
    power INT,
    age INT,
    predicted_price INT
)
"""

cur = conn.cursor() 
cur.execute(query_to_create_table) 
print("Your database and table are created!")
cur.close() 
conn.close()


