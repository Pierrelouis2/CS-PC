import os,sys

for i in range(4) :
    pid = os.fork()
    if pid != 0 :
        print("0k !")
    print("bonjour")

sys.exit(0)