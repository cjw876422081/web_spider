#-*-coding:utf-8-*-
import pymysql

db = pymysql.connect(host = 'localhost' , user = 'root' , password = 'cjw271118' , port=3306 , db='spiders')
cursor = db.cursor()

table = 'students'
condition = 'age > 20'

sql = 'select from (table) where (condition)'.format(table = table , condition = condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()