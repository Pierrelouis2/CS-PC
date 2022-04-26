import os,sys

if os.fork() == 0 :
    os.execlp("python","python","./TP1/miroir.py","test","ecart")

sys.exit(0)