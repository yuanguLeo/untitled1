#!/usr/bin/env python
#_*_coding:utf-8_*_

#当程序遇到问题时，不让程序结束，越过错误继续向下执行

'''
try''''''except''''''else

格式：
try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e:
    语句2
except 错误码 as e:
    语句n
else:
    语句e

注意：else语句可有可无

作用： 用来检测try语句块中的错误，从而让except语句来捕获错误信息，并处理

逻辑：当程序执行到try-except-else语句时
1、如果当try“语句t”执行出现错误，会匹配第一个错误码，如果匹配上就执行，对应的“语句”
2、如果当try“语句t”执行出现错误，没有匹配的异常，错误将会被提交到上一层的try语句，或者到程序的最上层
3、如果当try"语句t"执行没有出现错误，执行else下的“语句e”

'''


try:
    print(3 / 0)
    #print(num)
except NameError:
    print("没有该变量名称")
except ZeroDivisionError as e :
    print("除数为0了")
else:
    print("代码没有问题")

print("*************")

#使用except而不使用任何的错误类型
try:
    print(3 / 0)
except:
    print("程序出现错误！")

print("*******************")


#使用except带着多种异常
try:
    print(3 / 0)
except(NameError,ZeroDivisionError):
    print("程序出现了NameError或ZeroDivisionError错误")

print("*******************")


#特殊
'''
1、错误其实是class(类)，所有的错误都继承自BaseException，
所以在捕获的时候，它捕获了该类型的错误，还把子类一网打尽
'''
try:
    print(5 / 0)

except BaseException as e :
    print("异常1")

except ZeroDivisionError as e:
    print("异常2")


'''
2、跨越多层调用，

'''

def func1(num):
    print( 1 / num)

def func2(num):
    func1(num)

def main():
    func2(0)

try:
    main()
except ZeroDivisionError as e :
    print("**##")