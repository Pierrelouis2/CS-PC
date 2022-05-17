import multiprocessing as mp

def rdv(sem1,sem2,sem3,nb) :
    sem1.release()
    sem2.release()
    print(sem1,sem2,sem3,"nb rdv : p",nb)
    sem3.acquire()
    sem3.acquire()
    print(sem1,sem2,sem3,"rdv : p",nb)


if __name__ == '__main__':
    sem1 = mp.Semaphore(0)
    sem2 = mp.Semaphore(0)
    sem3 = mp.Semaphore(0)

    p1 = mp.Process(target=rdv, args=(sem1,sem2,sem3,1))
    p2 = mp.Process(target=rdv, args=(sem2,sem3,sem1,2))
    p3 = mp.Process(target=rdv, args=(sem3,sem1,sem2,3))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()  
    p3.join()