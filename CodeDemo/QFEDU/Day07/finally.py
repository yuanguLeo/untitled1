#!/usr/bin/env python
#_*_coding:utf-8_*_

'''

try''''''except''''''finlly

格式：
try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e:
    语句2
except 错误码 as e:
    语句n
finlly:
    语句f

作用：语句t无论是否有错误都将执行最后的语句f



'''


try:
    print(1/0)
except ZeroDivisionError as e:
    print("为0了")
finally:
    print("必须执行我")
