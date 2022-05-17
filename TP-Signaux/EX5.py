import signal,time,sys,os
import multiprocessing as mp

def arreterProgramme(signal, frame):
    """Fonction appelée quand vient l'heure d’arrêter notre programme"""
    print("  C'est l'heure d’arrêt !")
    sys.exit(0)

def F(s, frame):
    while True:
        time.sleep(1)
        print("boucle du fils")    
        signal.signal(signal.SIGINT, arreterProgramme)

Process = mp.Process(target= F, args =(None,None))

Process.start()

for i in range(5):
    time.sleep(1)
    print(f"tour n° {i}")

        