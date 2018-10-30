#Author:Wl
#coding=utf-8
# 定义一个进程列表
process_lst = []

def getProcess(pName):
    # 获取当前系统所有进程id列表
     all_pids  = psutil.pids()
     print (all_pids)

    # 遍历所有进程，名称匹配的加入process_lst
     for pid in all_pids:
        p = psutil.Process(pid)
        if (p.name() == pName):
            process_lst.append(p)

     return process_lst

# 获取进程名位Python的进程对象列表
     process_lst = getProcess("pycharm")

# 获取内存利用率：
for process_instance in process_lst:
    print process_instance.memory_percent()

# 获取cpu利用率：
for process_instance in process_lst:
    process_instance.cpu_percent(None)

    sleep(2)
for process_instance in process_lst:
    print process_instance.cpu_percent(None)

#作者：测试你个头
#链接：https://www.jianshu.com/p/23c2a518019a
#來源：简书
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。