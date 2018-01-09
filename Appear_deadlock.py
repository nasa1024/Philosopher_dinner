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


#服务生算法
def waiter():
    pool = Pool(processes=2)
    for x in Philosophers:
        pool.apply_async(Eating, (x,))

    pool.close()
    pool.join()

#吃饭
def Eating(who):
    print(str(who) + '正在吃饭')
    time.sleep(random.randint(0,20))#0到20秒的随机吃饭时间
    print(who ,"吃饱啦")

#思考(等待）
def Thinking(who):
    print(str(who) + '正在思考')
    time.sleep(1)
    print(who, " 想到了")


if __name__ == "__main__":
    #process_mutual_exclusion()
    waiter()


