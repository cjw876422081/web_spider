
#-*-coding:utf-8-*-

import json
import  urllib3
http = urllib3.PoolManager()

r = http.request( "GET" , "http://httpbin.org/headers" ,
                  headers={
                      "X-Something":"values"
                  })
print(json.loads(r.data.decode("utf-8"))["headers"])

r1 = http.request( "GET" , "http://httpbin.org/get" ,
                  fields={
                      "arg":"value"
                  })
print(json.loads(r1.data.decode("utf-8"))["args"])