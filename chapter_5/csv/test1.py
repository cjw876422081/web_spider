#-*-coding:utf-8-*-

import  csv

with open('data.csv' , 'w') as csvfile :
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])


#修改列与列之间的分隔符

with open('data.csv' , 'w') as csvfile :
    writer = csv.writer(csvfile  , delimiter = ' ')
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])

