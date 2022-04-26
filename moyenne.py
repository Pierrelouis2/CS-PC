import sys
from tkinter.tix import INTEGER
tot = 0
passe = True
if len(sys.argv[1:]) ==0 :
    print("aucune moyenne a calculer")

else :
    for i in sys.argv[1:] :
        if i.isdigit() : 
            if (int(i)<0) or (int(i) >20) :
                print("note(s) non valide(s)")
                passe = False
                break
            else:
                tot +=  int(i)
        else :
            print("note(s) non valide(s) digit")
            passe = False
            break
    if passe :
        moy = float(tot/(len(sys.argv)-1))
        print(moy)
        print ("Moyenne = %.2f" %moy)