import os,sys

if os.fork() == 0 :
    os.execlp('who','who')
pid,status = os.wait()
if os.fork() == 0 :
    os.execlp('ps','ps')
pid,status = os.wait()
os.execlp('ls','-l')