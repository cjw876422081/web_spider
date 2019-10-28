#-*-coding:utf-8-*-
import urllib3
import  json
http = urllib3.PoolManager()
response = http.request("GET" , "http://httpbin.org/robots.txt")
print(response.data) #返回数据内容
print(response.status)#状态码
print(response.headers)
print()

#在此同时发送其他类型的请求的数据，包括JSON，文件和二进制数据
response = http.request("POST" ,    "http://httpbin.org/post" , fields={"hello" :"world"})
print(response.data)
print(response.status)
print(response.headers)


print("\n")
response1 = http.request("GET" , "http://httpbin.org/ip")
print(json.loads(response.data.decode("utf-8")))


response2 = http.request("GET" , "http://httpbin.org/bytes/8")
print(response2.data)