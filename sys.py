#!/bin/python
#-*- coding:utf-8 -*-
#获取系统变量环境
'''
import sys
#print (sys.path)
print (sys.argv[2]) 
'''
#获取系统变量
import os
'''
cmd_res = os.system("pwd")#执行命令，不保存结果
'''

cmd_res = os.popen("pwd").read()
print ("->>",cmd_res)
os.mkdir("netwen.tx")#创建一个新文件


