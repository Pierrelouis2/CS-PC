import random, time
import os,math
import multiprocessing as mp


# calculer le nbr de hits dans un cercle unitaire (utilisé par les différentes méthodes)
def pi_multiprocess(verrou,nb_total_iteration):
    count = 0
    for i in range(nb_total_iteration):
        x = random.random()
        y = random.random()
    # si le point est dans l’unit circle
        if x * x + y * y <= 1: 
            count += 1
    verrou.acquire()
    compte.value += count
    verrou.release()

def frequence_de_hits_pour_n_essais(nb_iteration):
    count = 0
    for i in range(nb_iteration):
        x = random.random()
        y = random.random()
        # si le point est dans l’unit circle
        if x * x + y * y <= 1: count += 1
    return count
# Nombre d’essai pour l’estimation



if __name__ == '__main__': 
    
    nb_total_iteration = 10000000

    start = time.time()
    
   
    Nb_process = 50
    mes_process = [0 for i in range(Nb_process)]

    compte = mp.Value('f',0)

    verrou = mp.Semaphore(1)


    for i in range(Nb_process):  # Lancer     Nb_process  processus
            mes_process[i] = mp.Process(target=pi_multiprocess, args=(verrou,int(nb_total_iteration/Nb_process)))
            mes_process[i].start()

    for i in range(Nb_process): mes_process[i].join()

    end = time.time()
    pi = 4 * compte.value / nb_total_iteration
    print("val de pi en multi-process:",pi, "temps de calcul : ",math.floor(1000*(end-start))/1000," s")
    

    start = time.time()

    nb_hits=frequence_de_hits_pour_n_essais(nb_total_iteration)

    end = time.time()
    print("Valeur estimée Pi par la méthode Mono−Processus : ", 4 * nb_hits / nb_total_iteration,"temps de calcul : ",math.floor(1000*(end-start))/1000," s")

