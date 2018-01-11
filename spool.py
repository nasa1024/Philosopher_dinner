import threading
import os
import random

spool_queue = []#打印请求队列（用数组实现）
spool_in = None#记录下一个打印请求存放的位置
spool_out = None#记录下一个被打印文件的位置
#spool_count = len(spool_queue)#记录打印队列中的文件个数
sys_opreat = None
lock = threading.Lock()#申明进程锁


def sendthred(file_name):
    '''
    接收用户的打印请求并将其发送到打印请求队列中
    :return: 
    '''
    global spool_queue
    lock.acquire()
    try:
        spool_queue.append([file_name,random.randint(0,100)])
    finally:
        lock.release()



def spool_thread():
    '''
    从打印请求队列中取待打印文件并将其输出到屏幕上
    :return: 
    '''
    global spool_queue
    lock.acquire()

    print('print list num is ',len(spool_queue))
    length = spool_queue.pop()
    print("|--------|-------------------------------------|--------------|")
    print("| index  | filename                            | filesize(KB) |")
    print("|--------|-------------------------------------|--------------|")
    # for x in range(len(spool_queue)):
    print('|        |          %s                         |      %d      |' %(length[0],length[1]))
    print('|--------|-------------------------------------|--------------|')

    lock.release()

def print_space(n):
    '''
    显示若干个空格(没啥用）
    :return: 
    '''
    print(' ' * n)


def list_spool_queue():
    '''
    列出打印队列
    :return: 
    '''
    print(spool_queue)



def which_os_is():
    global sys_opreat
    if os.name == 'nt':
        sys_opreat = os.system('cls')
    else:
        sys_opreat = os.system('clear')

def main():
    '''
    创建线程，初始化信号量，显示主菜单，根据用户选择执行相应功能
    :return: 
    '''
    while True:
        print("|----------------------------|")
        print("|  1:send a print request    |")
        print("|  2:list spool queue        |")
        print("|  3:print a file in spool   |")
        print("|  4:exit                    |")
        print("|----------------------------|")
        a = int(input('select a  function '))
        try:
            if a == 1:
                file_name = input('亲输入文件名')
                t1 = threading.Thread(target=sendthred(file_name))
                t1.start()
                t1.join()
            elif a == 2:
                list_spool_queue()
            elif a == 3:
                t2 = threading.Thread (target=spool_thread())
                t2.start ()
                t2.join ()
            elif a == 4:
                break
        except:
            print('输入错误')
            main()




if __name__ == '__main__':
    mainthred = threading.Thread(target=main())#创建主线程
    mainthred.start()
    mainthred.join()



'''
参考：
    https://www.zhihu.com/question/23474039
    （python多线程鸡肋嘛？）
    http://python.jobbole.com/85050/
    （python多线程实现）
    
    对于多线程来说，最大的特点就是线程之间可以共享数据，那么共享数据就会出现多线程同时更改一个变量，使用同样的资源，而出现死锁、数据错乱等情况。
假设有两个全局资源，a和b，有两个线程thread1，thread2. thread1占用a，想访问b，但此时thread2占用b，想访问a，两个线程都不释放此时拥有的资源，
那么就会造成死锁。
对于该问题，出现了Lock。 当访问某个资源之前，用Lock.acquire()锁住资源,访问之后，用Lock.release()释放资源。

    虽然Python多线程有缺陷，总被人说成是鸡肋，但也不是一无用处，它很适合用在IO密集型任务中。I/O密集型执行期间大部分是时间都用在I/O上，如数据库I/O，
较少时间用在CPU计算上。因此该应用场景可以使用Python多线程，当一个任务阻塞在IO操作上时，我们可以立即切换执行其他线程上执行其他IO操作请求。
'''
