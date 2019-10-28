#-*-coding:utf-8-*-

import  re

content = "Hello 123 4567 World_This is a Regex Demo"
print(len(content))

result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}' , content)
print(result)
print(result.group())
print(result.span())



content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld', content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())




#t贪婪
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$', content)
print(result)
print(result.group(1))

#不贪婪
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo$', content)
print(result)
print(result.group(1))



content  = '''Hello 1234567 World_This
is a Regex Demo
'''

result = re.match("^He.*?(\d+).*?Demo$" , content ,re.S)
print(result.group(1))
