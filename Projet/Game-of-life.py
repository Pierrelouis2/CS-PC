import multiprocessing as mp
import random as rand
import sys,time
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

# Définition de qq fonctions de gestion de l'écran
def effacer_ecran() : print(CLEARSCR,end='')
def erase_line_from_beg_to_curs() : print("\033[1K",end='')
def curseur_invisible() : print(CURSOFF,end='')
def curseur_visible() : print(CURSON,end='')
def move_to(lig, col) : print("\033[" + str(lig) + ";" + str(col) + "f",end='')

def en_couleur(Coul) : print(Coul,end='')
def en_rouge() : print(CL_RED,end='') # Un exemple !


def main():



    pass

def next_generation(LIGNES,COLONNES,GRID) :

    # on passe a travers toutes les cases de la grid
    for l in range(LIGNES):
        for c in range(COLONNES):



            # on cherche le nombre de voisins vivant
            voisin_vivant = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    if ((l+i>=0 and l+i<LIGNES) and (c+j>=0 and c+j<COLONNES)):
                        voisin_vivant += GRID[l + i][c + j]
    
            voisin_vivant -= GRID[l][c]

            #case seul et meurs
            if GRID[l][c] == 1 and voisin_vivant < 2 :
                GRID[l][c] = 0
            
            #case avec trop de voisin_vivant
            if GRID[l][c] == 1 and voisin_vivant > 3 :
                GRID[l][c] = 0
            
            #case morte avec 3 voisins qui revit
            if GRID[l][c] == 0 and voisin_vivant == 3 :
                GRID[l][c] = 1

    s_grid.send(GRID)
    sys.exit(0)
    
def display(GRID,LIGNES,COLONNES):
    effacer_ecran()

    for p in range(COLONNES) :
        for j in range(LIGNES):
                if GRID[p][j] == 1 :
                    GRID[p][j] = '#'
                else :
                    GRID[p][j] =' '
    for i in range(len(GRID)):
        
        move_to(i+5,0)
        print(' '.join(GRID[i]))
    sys.exit(0)




if __name__ == '__main__':

    LIGNES= 50
    COLONNES = 100
    proba = [0 for i in range(15)]
    proba[0] = 1
    GRID_i = [[rand.choice(proba) for i in range(COLONNES)] for j in range(LIGNES)]
    r_grid,s_grid = mp.Pipe()
    gen_numb =0
    while True :
        next_gen = mp.Process(target =next_generation, args =(LIGNES,COLONNES,GRID_i))
        next_gen.start()
        next_gen.join()

        disp = mp.Process(target=display, args=(GRID_i,COLONNES,LIGNES))
        disp.start()
        disp.join()
        GRID_i = r_grid.recv()
        gen_numb +=1
        print(gen_numb)
        time.sleep(0.2)
