# Cours hippique
# Version très basique, sans mutex sur l'écran, sans arbitre, sans annoncer le gagant, ... ...

# Quelques codes d'échappement (tous ne sont pas utilisés)
CLEARSCR="\x1B[2J\x1B[;H"          #  Clear SCreen
CLEAREOS = "\x1B[J"                #  Clear End Of Screen
CLEARELN = "\x1B[2K"               #  Clear Entire LiNe
CLEARCUP = "\x1B[1J"               #  Clear Curseur UP
GOTOYX   = "\x1B[%.2d;%.2dH"       #  ('H' ou 'f') : Goto at (y,x), voir le code

DELAFCURSOR = "\x1B[K"             #  effacer après la position du curseur
CRLF  = "\r\n"                     #  Retour à la ligne

# VT100 : Actions sur le curseur
CURSON   = "\x1B[?25h"             #  Curseur visible
CURSOFF  = "\x1B[?25l"             #  Curseur invisible

# Actions sur les caractères affichables
NORMAL = "\x1B[0m"                  #  Normal
BOLD = "\x1B[1m"                    #  Gras
UNDERLINE = "\x1B[4m"               #  Souligné


# VT100 : Couleurs : "22" pour normal intensity
CL_BLACK="\033[22;30m"                  #  Noir. NE PAS UTILISER. On verra rien !!
CL_RED="\033[22;31m"                    #  Rouge
CL_GREEN="\033[22;32m"                  #  Vert
CL_BROWN = "\033[22;33m"                #  Brun
CL_BLUE="\033[22;34m"                   #  Bleu
CL_MAGENTA="\033[22;35m"                #  Magenta
CL_CYAN="\033[22;36m"                   #  Cyan
CL_GRAY="\033[22;37m"                   #  Gris

# "01" pour quoi ? (bold ?)
CL_DARKGRAY="\033[01;30m"               #  Gris foncé
CL_LIGHTRED="\033[01;31m"               #  Rouge clair
CL_LIGHTGREEN="\033[01;32m"             #  Vert clair
CL_YELLOW="\033[01;33m"                 #  Jaune
CL_LIGHTBLU= "\033[01;34m"              #  Bleu clair
CL_LIGHTMAGENTA="\033[01;35m"           #  Magenta clair
CL_LIGHTCYAN="\033[01;36m"              #  Cyan clair
CL_WHITE="\033[01;37m"                  #  Blanc
#-------------------------------------------------------
import multiprocessing as mp
 
import os, time,math, random, sys, ctypes, signal

# Définition de qq fonctions de gestion de l'écran
def effacer_ecran() : print(CLEARSCR,end='')
def erase_line_from_beg_to_curs() : print("\033[1K",end='')
def curseur_invisible() : print(CURSOFF,end='')
def curseur_visible() : print(CURSON,end='')
def move_to(lig, col) : print("\033[" + str(lig) + ";" + str(col) + "f",end='')

def en_couleur(Coul) : print(Coul,end='')
def en_rouge() : print(CL_RED,end='') # Un exemple !

#-------------------------------------------------------
# La tache d'un cheval
def un_cheval(ma_ligne : int, keep_running,lst_positions,verrou) : # ma_ligne commence à 0
    col=1
    dessin = ["    °",'-('+chr(ord('A')+ma_ligne)+'>',"/  /"]
    
    while col < LONGEUR_COURSE and keep_running.value :
        verrou.acquire()
        for i,d in enumerate(dessin) :
            move_to(ma_ligne*len(dessin)+1+i,col)         # pour effacer toute ma ligne
            erase_line_from_beg_to_curs()
            en_couleur(lyst_colors[ma_ligne%len(lyst_colors)])
            print(d)
        lst_positions[ma_ligne] = col
        verrou.release()

        col+=1

        try : # En cas d'interruption
            time.sleep(0.1 * random.randint(1,5))
        finally : 
            pass

#------------------------------------------------   
def prise_en_compte_signaux(signum, frame) :
    # On vient ici en cas de CTRL-C p. ex.
    move_to(Nb_process+11, 1)
    print(f"Il y a eu interruption No {signum} au clavier ..., on finit proprement")
    
    for i in range(Nb_process): 
        mes_process[i].terminate() 
    
    move_to(Nb_process+12, 1)
    curseur_visible()
    en_couleur(CL_WHITE)
    print("Fini")
    sys.exit(0)
# ---------------------------------------------------
def arbitre(lst_positions,verrou,keep_running) :
    ind_maxi = 0
    ind_mini = 0
    while keep_running :
        
        verrou.acquire()
        lst=lst_positions[:]
        verrou.release()
        if lst[ind_maxi] != LONGEUR_COURSE - 1 :
            maxi=max(lst)
            ind_maxi=lst.index(maxi)
        
        if lst[ind_mini] != LONGEUR_COURSE - 1 :
            mini = min(lst)
            ind_mini = lst.index(mini)


        verrou.acquire()
        move_to(Nb_process+12, 1)
        erase_line_from_beg_to_curs()
        print("le cheval le plus rapide est : ",'('+chr(ord('A')+ind_maxi)+'>',"le cheval le plus lent est : ",'('+chr(ord('A')+ind_mini)+'>')
        verrou.release()
        if lst[ind_mini] == LONGEUR_COURSE -1 :
            keep_running = False
            if PARI == chr(ord('A')+ind_maxi) :
                move_to(Nb_process+13, 1)
                erase_line_from_beg_to_curs()
                print("pari gagnant")
            else :
                move_to(Nb_process+13, 1)
                erase_line_from_beg_to_curs()
                print("pari perdu")
        try :
            time.sleep(0.1 * random.randint(1,5))
        finally :
            pass
        





# ---------------------------------------------------
# La partie principale :
if __name__ == "__main__" :
    
    # Une liste de couleurs à affecter aléatoirement aux chevaux
    lyst_colors=[CL_WHITE, CL_RED, CL_GREEN, CL_BROWN , CL_BLUE, CL_MAGENTA, CL_CYAN, CL_GRAY,
                CL_DARKGRAY, CL_LIGHTRED, CL_LIGHTGREEN,  CL_LIGHTBLU, CL_YELLOW, CL_LIGHTMAGENTA, CL_LIGHTCYAN]
    
    LONGEUR_COURSE = 100 # Tout le monde aura la même copie (donc no need to have a 'value')
    keep_running=mp.Value(ctypes.c_bool, True)

    Nb_process=4
    mes_process = [0 for i in range(Nb_process)]
    lst_positions = mp.Array('i',Nb_process)
 
    signal.signal(signal.SIGQUIT , prise_en_compte_signaux)

    effacer_ecran()
    curseur_invisible()

    verrou = mp.Semaphore(1)

    PARI = input("qui sera la gagnant : (lettre en majuscule) ")
    start = input("depart : T ? F ?")

    if start == "T" :


        for i in range(Nb_process):  # Lancer     Nb_process  processus
            mes_process[i] = mp.Process(target=un_cheval, args= (i,keep_running,lst_positions,verrou))
            mes_process[i].start()

        move_to(Nb_process+10, 1)
        print("tous lancés, Controle-C pour tout arrêter")

        proc_arbitre = mp.Process(target = arbitre,args=(lst_positions,verrou,keep_running))
        proc_arbitre.start()
        

        # On attend la fin de la course
        for i in range(Nb_process): mes_process[i].join()
        proc_arbitre.join()
        move_to(Nb_process+14, 1)
        curseur_visible()
        print("Fini")
