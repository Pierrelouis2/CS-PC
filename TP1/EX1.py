

import sys

print("nom du programme : ",sys.argv[0])
print("nombre d'argument : ",len(sys.argv)-1)
print("les arguments sont : ")
for arg in sys.argv[1:] :
    print(arg)
print(sys.argv)