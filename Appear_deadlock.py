import os
import time
import random
from multiprocessing import Process,Pool

Philosophers = ['马克思1','苏格拉底2','拉格朗日3','莱布尼茨4','亚里士多德5']

def process_mutual_exclusion():
    '''
    进程互斥
    此函数只能在 unix/linux 下运行，因为调用的是linux创建进程的API。
    windows 下只能调用相关进程包。
    :return: ioerror
    '''
    with open('README.md','a') as f:
        try:
            processid = os.fork()
            if processid:
                print(f.read())
            else:
                print(f.read())
        except IOError:
            print(IOError.args)


#服务生算法异步算法
def waiter_async():
    '''
    服务生算法，统一把资源收起来。交给操作系统调度。异步方法。
    :return: none/
    '''
    pool1 = Pool(processes=2)
    for x in Philosophers:
        pool1.apply_async(Eating, (x,))

    pool1.close()
    pool1.join()

#服务生算法同步方法(管程）
def waiter_synchro():
    '''
    同步方法
    :return:
    '''
    pool2 = Pool(processes=2)
    for x in Philosophers:
        pool2.apply(Eating, (x,))

    pool2.close()
    pool2.join()


#吃饭
def Eating(who):
    print(str(who) + '正在吃饭')
    time.sleep(random.randint(0,3))#0到20秒的随机吃饭时间
    print(who ,"吃饱啦")




if __name__ == "__main__":
    # 第一个函数是 进程互斥的实例 第二个函数是 哲学家问题同步解决方法
    #process_mutual_exclusion()
    #waiter_synchro()
    waiter_async()




