import multiprocessing as mp

def rdv(sem1,sem2) :
    sem1.release()
    sem2.acquire()
    print(sem1,sem2,"rdv")


if __name__ == '__main__':
    sem1 = mp.Semaphore(0)
    sem2 = mp.Semaphore(0)


    p1 = mp.Process(target=rdv, args=(sem1,sem2))
    p2 = mp.Process(target=rdv, args=(sem2,sem1))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
