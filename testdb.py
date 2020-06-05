# author:ToddCombs
import sqlite3
conn = sqlite3.connect('sqlite.db')
c = conn.cursor()
print("数据库连接成功")
conn.commit()
conn.close()