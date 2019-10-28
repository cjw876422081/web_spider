#-*-coding:utf-8-*-

import pymysql

db = pymysql.connect(host = 'localhost' , user = 'root' , password = 'cjw271118' , port=3306 , db='spiders')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
cursor.execute(sql)
db.close()