import os,sys



for i in range (3) :
    pid = os.fork()
    if pid == 0 :
        print("je suis ",os.getpid(),"mon pere est ",os.getppid(),"retour : ",pid)
        break
sys.exit(0)