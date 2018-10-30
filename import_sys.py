#!/bin/python
'''
java 先编辑成字节码文件，然后运行通过解释成机器语言，先预先编译一部分（半成品）
Python执行之前第一项工作和java一样的，但是边执行边编译
当Python程序运行时，编译结果则是保存于内存的pycodeobject中，当程序结束时，写入硬盘中.pyc
程序运行时判断更新来确定程序是否最新
'''
#import math
'''
一.数据类型
1.数字
type(2*64)  type()读取数据类型
int整型 long长整型
’‘’