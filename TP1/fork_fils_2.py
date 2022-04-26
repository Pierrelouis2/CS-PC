import os,sys


N = 10


for i in range (N) :
    pid = os.fork()
    if pid == 0 :
        print("je suis ",os.getpid(),"mon pere est ",os.getppid())
        break
sys.exit(0)
