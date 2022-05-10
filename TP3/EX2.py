import multiprocessing as mp
import os,sys

(dfr,dfw) = mp.Pipe( ) 
pid = os.fork()
if pid != 0 :
    print ("[Le processus %d] : ls \n" %os.getpid() )
    dfr.close()
    os.dup2(dfw.fileno() , sys.stdout.fileno())
    dfw.close()
    os.execlp("cat" , "cat","TP3/EX1.py") 
else :
    print ("[Le processus %d] : wc \n" %os.getpid() )
    dfw.close() 
    os.dup2(dfr.fileno() , sys.stdin.fileno() ) 
    dfr.close() 
    os.execlp("wc" , "wc")

sys.exit(0)