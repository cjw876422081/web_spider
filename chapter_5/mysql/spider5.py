#-*-coding:utf-8-*-
import pymysql

db = pymysql.connect(host = 'localhost' , user = 'root' , password = 'cjw271118' , port=3306 , db='spiders')
cursor = db.cursor()

sql = 'update students set age = %s where name  = %s'
try :
    cursor.execute(sql ,(25 ,'Bob'))
    db.commit()
except:
    db.rollback()
db.close()



