import time
import random
from multiprocessing import Process,Event,Pipe

class Philosopher():
    def __init__(self,id,e):
        self.forkleft = False
        self.forkright = False
        self.thinking = random.randint(5)
        self.eating = random.randint(3)
        self.id = id
        self.e = e

    def thinking(self):
        print(id,' 号正在思考')
        self.e.wait(self.thinking)


    def eating(self):

        pass


    def begin(self):
        p1 = Process(target=self.Chandy_misra,args=())








if __name__ == "__main__":

    pass
#https://docs.python.org/2.7/library/multiprocessing.html
#https://docs.python.org/2.7/library/threading.html#threading.Event
#http://python.jobbole.com/82045/
#https://baike.baidu.com/item/%E5%93%B2%E5%AD%A6%E5%AE%B6%E5%B0%B1%E9%A4%90%E9%97%AE%E9%A2%98/10929794

