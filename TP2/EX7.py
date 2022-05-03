import os,sys

N = 2
for i in range(N) :
#__________début des ajouts_________
    for i in range(3) :
        if os.fork() != 0 :
            break
# __________fin des ajouts__________
print("Bonjour")
sys.exit(0)