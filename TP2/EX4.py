import os,sys
n=0
for i in range(1,5) :
    fils_pid = os.fork() #1
    if (fils_pid > 0) : #2 on reste dans le pere
        os.wait() #3 fais que le programme est deterministe
        n = i*2
        break
print("n = ", n) #4
sys.exit(0)