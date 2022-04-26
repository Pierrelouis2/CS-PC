import os,sys

N = 10
i = 2

while os.fork() == 0 and i<N :
    i += 1
    print("je suis ",os.getpid(),"mon pere est ",os.getppid())
sys.exit(0)
