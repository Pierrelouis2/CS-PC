import signal,time,sys,os
import multiprocessing as mp

def F():
    while True:
        time.sleep(1)
        print("boucle du fils")    

Process = mp.Process(target= F, args =())

Process.start()

for i in range(5):
    time.sleep(1)
    print(f"tour n° {i}")
    if i ==3:
        print("Processus [%d] envoi le signal %d au processus %d" %(os.getpid(), signal.SIGKILL, Process.pid))
        os.kill(Process.pid,signal.SIGKILL)
