import multiprocessing as mp
import sys

def rdv():
    


if __name__ == '__main__':
    sem = [mp.Semaphore(0) for i in range(sys.argv[1])]
    process = [mp.Process(target=rdv) for i in range(sys.argv[1])]

    for j in process:
        process.start()
        process.join()
    





