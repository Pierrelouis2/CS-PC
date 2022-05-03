import os,sys

dicoNotes = { "E1" : [10, 15, 20], "E2" : [12, 16, 15], "E3" : [11, 13, 20]}


for i in dicoNotes :
    moy=0
    if os.fork() == 0 : 
        for j in dicoNotes[i] :
            moy+= j
        moy = moy/len(dicoNotes[i])
        print(moy,i)
        break