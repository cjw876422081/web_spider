#-*-coding:utf-8-*-

import pymysql

db = pymysql.connect(host='localhost',user='root', password='cjw271118', port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET UTF8MB4")
db.close()
