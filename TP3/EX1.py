import os,sys
import multiprocessing as mp

text = "coucou"

(dfr,dfw) = mp.Pipe()
n = dfw.send(text)

print ("Le processus %d a transmis le message %s\n" %(os.getpid() , text ) )
textRecu = dfr.recv()
print ("Le processus %d a reçu le message %s\n" %(os.getpid() , textRecu))

dfr.close( ) ; dfw.close( )
sys.exit(0)