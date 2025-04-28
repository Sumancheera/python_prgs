# multithreading in python 
from time import sleep
from threading import *
class Hello(Thread):  # if hello() is sub class of thread class then we can create 2 diffrent threads
    def run(self):
        for i in range(50):
            print("hello")
            sleep(1)  # sleep for t1 thread
class Hi(Thread):
    def run(self):
        for i in range(50):
            print("hi")
            sleep(1)   ## sleep for t2 thread
t1=Hello()
t2=Hi()

# t1.run()
# t2.run()
t1.start()
sleep(0.2)  # sleep for main thread
t2.start()

print("end")

