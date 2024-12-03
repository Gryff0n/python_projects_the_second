from pyamaze import*
import os
import glob
import random
import pygetwindow as gw

class File:
    ''' classe File
    création d'une instance File avec une liste
    '''
    def __init__(self):
        self.L = []

    def vide(self):
        return self.L == []

    def defiler(self):
        assert not self.vide(), "file vide"
        return self.L.pop(0)

    def enfiler(self,x):
        self.L.append(x)

    def taille(self):
        return len(self.L)

    def sommet(self):
        return self.L[0]
        
    def present(self,x):
        return x in self.L
    
    def show(self):
        return self.L

class Pile:
    ''' classe Pile
    création d'une instance Pile avec une liste
    '''
    def __init__(self):
        self.L = []
    def vide(self):
        return self.L == []
    def depiler(self):
        assert not self.vide(),"Pile vide"
        return self.L.pop()
    def sommet(self):
        assert not self.vide(),"Pile vide"
        return self.L[-1]
    def empiler(self,x):
        self.L.append(x)

def initialisation() :
    """
    La permière fonction appelée, elle sert a créer le labyrinthe et
    le stock dans le dossier du projet sous la forme d'un fichier csv.
    """
    global map, lar, lon

    #On supprime d'abord les précédents fichiers csv potentiellement restants d'une exécution précédente.
    for past_files in glob.glob('*.csv') :
        os.remove(past_files)
    #on demande a l'utilisateur la longueur souhaitée pour le labyrinthe, tout en vérifiant que celle ci est un entier positif.
    lon = input("Bienvenue, tout d'abord, veuillez créé un labyrinthe. Longueur du labyrinthe ?\n>>>")
    while lon.isnumeric() == False or not int(lon) > 0 :
        lon = input("Veuillez rentrer un nombre. Longueur du labyrinthe ?\n>>>")
    lon = int(lon)
    #on demande a l'utilisateur la largeur souhaitée pour le labyrinthe, tout en vérifiant que celle ci est un entier positif.
    lar = input("Largeur du labyrinthe ?\n>>>")
    while lar.isnumeric() == False or not int(lar) > 0  :
        lar = input("Veuillez rentrer un nombre. Largeur du labyrinthe ?\n>>>")
    lar = int(lar)
    #on demande a l'utilisateur le taux de boucle souhaitée pour le labyrinthe,
    #de 1 a 100, plus le nombre est élevé et plus il y aura de cycles, 0 donne un labyrinthe parfait.
    loop = input("taux de boucle au sein de labyrinthe (de 0 a 100) ?\n>>>")
    while loop.isnumeric() == False or int(loop) < 0 or int(loop) > 100 :   #on vérifie que le nombre est entier et compris entre 0 et 100
        loop = input("Veuillez rentrer un nombre. taux de boucle au sein de labyrinthe (de 0 a 100) ?\n>>>")
    loop = int(loop)
    m=maze(lar,lon)         #on créé les bordures du labyrinthe au dimensions souhaitée et on affiche le résultat a l'utilisateur
    print("Voici votre labyrinthe :")
    m.CreateMaze(saveMaze= True, loopPercent=loop)  #on sauvegarde la disposition du labyrinthe sous forme de fichier csv
    b=agent(m,filled=True, color=COLOR.dark, x=1, y=1)
    #on stocke les informations des endroits ou se trouvent les murs case par case, sous forme de dictionnaire de dictionnaires.
    map = m.maze_map
    menu()      #on appelle le menu

def menu() :
    """
    Fonction passerelle reliant les différentes opérations possibles sur le labyrinthe, a savoir
    les différents parcours, le résolution, la détection de cycle, et la création d'un nouveau
    labyrinthe, remplaçant l'ancien. On peut aussi arrêter le programme depuis ce menu.
    """

    #On demande tout d'abord ce que souhaite faire l'utilisateur.
    y = input("que souhaitez vous faire ?\n0 - Arrêt du programme\n1 - parcours de labyrinthe \n2 - résolution de labyrinthe\n3 - détection de cycle\n4 - créer un nouveau labyrinthe\n>>>")
    while y not in ["0","1","2","3","4"] :
        y = input("Veuillez choisir parmi ce qui vous est proposé.\n0 - Arrêt du programme\n1 - parcours\n2 - résolution\n3 - détection de cycle\n4 - créer un nouveau labyrinthe\n>>>")
    if y == "0" :
        #si l'utilisateur souhaite arrêter le programme, on supprime le csv sauvegardé et on arrête l'exécution.
        result = glob.glob('*.csv') 
        file = result[0]
        os.remove(file)
        exit()
    if y == "1" :
        #cette option mène au menu des parcours de labyrinthe.
        parcours()
    if y == "2" :
        #cette option mène a la fonction de résolution du labyrinthe.
        resolution()
    if y == "3" :
        #cette option révèle instantanément si le labyrinthe possède le moindre cycle ou si il est acyclique.
        cycle()
    if y == "4" :
        #cette option relance la fonction d'initialisation dans le but de créer un nouveau labyrinthe.
        initialisation()

def parcours() :
    """
    Cette fonction est un sous-menu dédié aux différents algorithme possible pour parcourir le labyrinthe.
    """
    #le labyrinthe étant détruit a chaque fois que l'utilisateur ferme la fenêtre, on le recréé.
    m=maze(lar,lon)         
    result = glob.glob('*.csv')
    file = result[0]
    #on donne le choix a l'utilisateur sur la manière pour parcourir le labyrinthe
    x = input("Comment souhaitez vous parcourir le labyrinthe ?\n 0 - Menu Principal\n 1 - Parcours en largeur (BFS)\n 2 - Parcours en Profondeur (DFS)\n>>>")
    while x not in ["0","1","2"] :
        x = input("Veuillez choisir parmi ce qui vous est proposé.\n 0 - Menu Principal\n 1 - Parcours en largeur (BFS)\n 2 - Parcours en Profondeur (DFS)\n>>>")
    if x == "0" :
        menu()
    elif x == "1" :
        #cette option lance le parcours en largeur du labyrinthe.
        m.CreateMaze(loadMaze= file)
        bfs=parcours_largeur(m.maze_map, (m.rows,m.cols))
        a=agent(m,filled=True,footprints=True, goal=bfs[len(bfs)-1])
        m.tracePath({a : bfs}, delay=int((1/((lar+lon)/2))*150))
        b=agent(m,filled=True, color=COLOR.dark, x=1, y=1)
        m.run()
        #on revient au sous-menu de parcours.
        parcours()
    elif x == "2" :
        #cette option lance le parcours en profondeur du labyrinthe.
        m.CreateMaze(loadMaze= file)
        dfs=parcours_profondeur(m.maze_map, (m.rows,m.cols))
        a=agent(m,filled=True,footprints=True, goal=dfs[len(dfs)-1])
        m.tracePath({a : dfs}, delay=int((1/((lar+lon)/2))*300))
        b=agent(m,filled=True, color=COLOR.dark, x=1, y=1)
        m.run()
        #on revient au sous-menu de parcours.
        parcours()        


def voisins(m,case):
    """
    cette fonction, utile pour les algorithmes a venir, renvoie la liste des voisins d'une case,
    en ajoutant ou retirant 1 a la coordonnée correspondante en se servant des informations contenues
    dans le dictionnaire map.
    """
    voisins = []
    if m[case]['E'] == 1 :
        voisins.append((case[0], case[1]+1))
    if m[case]['W'] == 1 :
        voisins.append((case[0], case[1]-1))
    if m[case]['N'] == 1 :
        voisins.append((case[0]-1, case[1]))
    if m[case]['S'] == 1 :
        voisins.append((case[0]+1, case[1]))
    return voisins


def parcours_largeur(G, sommet):
    """
    cette fonction effectue un parcours en largeur sur le labyrinthe, ce qui signifie que l'on va partir d'une case
    (par défaut la coin inférieur droit du labyrinthe) et parcourir chaque case a 1 de distance de celle-ci, puis
    2 de distance, puis 3, etc...
    """
    #on créé une liste pour les sommets visités, qui correspondra a
    #la liste de case que l'agent va suivre pour parcourir le labyrinthe
    sommet_visite = [] 
    f = File()  #on créé une file pour y mettre les voisins de chaque case
    f.enfiler(sommet)
    while f.vide() == False:
        tmp = f.defiler()
        if tmp not in sommet_visite:
            sommet_visite.append(tmp)
        #on parcours chaque case voisine dans la file.
        for vois in voisins(G,tmp):
            if vois not in sommet_visite and f.present(vois) == False:
                f.enfiler(vois)
    return sommet_visite


def parcours_profondeur(G, sommet):
    """
    cette fonction effectue un parcours en profondeur sur le labyrinthe, ce qui signifie que l'on va partir d'une case
    (par défaut la coin inférieur droit du labyrinthe) et parcourir un seul chemin jusqu'au bout avant de parcourir les
    chemin oubliés.
    """
    #on créé une liste pour les sommets visités, qui correspondra a
    #la liste de case que l'agent va suivre pour parcourir le labyrinthe
    sommets_visites = []
    sommets_fermes = []
    p = Pile()  #on créé une file pour y mettre les chemins non parcourus
    sommets_visites.append(sommet)
    p.empiler(sommet)
    while p.vide() == False:    
        tmp = p.sommet()
        voisins2 = [y for y in voisins(G,tmp) if y not in sommets_visites]
        if len(voisins2) != 0:
            v = random.choice(voisins2)
            sommets_visites.append(v)
            p.empiler(v)
        else:
            sommets_fermes.append(tmp)  #on dépile une fois le chemin actuel entièremment parcouru.
            p.depiler()
    return sommets_visites

sommets_visites_dfs2 = []       #liste et dictionnaire nécessaires pour les algorithmes à venir.
parents = dict()

def resolution() :
    """
    Cette fonction permet de trouver un chemin possible entre 2 cases du labyrinthe
    """
    m=maze(lar,lon)
    result = glob.glob('*.csv') #on recréé le labyrinthe a partir du csv
    file = result[0]
    #on rappelle les dimensions du labyrinthe
    print(f"Votre labyrinthe fait {lon} de long et {lar} de largeur, veuillez choisir des coordonnées valides.")
    #on demande a l'utilisateur les coordonnées de la case de départ en vérifiant que ce sont des nombres
    #compris entre 1 et le taille du labyrinthe.
    departx = input(f"coordonnée x de la case de départ de 1 a {lon} ?\n>>>")
    departy = input(f"coordonnée y de la case de départ (axe y inversé) de {lar} a 1 ?\n>>>")
    while not departx.isnumeric() or not departy.isnumeric() or (int(departy), int(departx)) not in map.keys() :
        print("COORDONNEES INVALIDES")
        departx = input(f"coordonnée x de la case de départ de 1 a {lon} ?\n>>>")
        departy = input(f"coordonnée y de la case de départ (axe y inversé) de {lar} a 1 ?\n>>>")
    #on créé la case départ
    depart = (int(departy), int(departx))
    arrivex = input(f"coordonnée x de la case d'arrivée de 1 a {lon} ?\n>>>")
    arrivey = input(f"coordonnée y de la case d'arrivée (axe y inversé) de {lar} a 1\n>>>")
    while not arrivex.isnumeric() or not arrivey.isnumeric() or (int(arrivey), int(arrivex)) not in map.keys() :
        print("COORDONNEES INVALIDES")
        arrivex = input(f"coordonnée x de la case d'arrivée de 1 a {lon} ?\n>>>")
        arrivey = input(f"coordonnée y de la case d'arrivée (axe y inversé) de {lar} a 1 ?\n>>>")
    #on créé la case d'arrivée
    arrivee = (int(arrivey), int(arrivex))
    parents[depart] = None
    #on exécute la fonction pour trouver le chemin
    s=Solution(arrivee, dfs2(map, depart))
    m.CreateMaze(loadMaze= file)
    a=agent(m,filled=True,footprints=True, goal=s[len(s)-1], color=COLOR.red, x=depart[0], y=depart[1])
    m.tracePath({a : s}, delay=100) #on trace le chemin a suivre.
    ar=agent(m,filled=True, color=COLOR.green, x=arrivee[0], y=arrivee[1])
    b=agent(m,filled=True, color=COLOR.dark, x=1, y=1)
    m.run()
    #on retourne au menu
    menu()

def dfs2(G, depart):
    """
    cette fonction est un parcours en profondeur fais de manière
    récursive tout en stockant les parents de chaque case dans un
    dictionnaire.
    """
    if depart not in sommets_visites_dfs2:
        sommets_visites_dfs2.append(depart)
    voisins2 = [y for y in voisins(G,depart) if y not in sommets_visites_dfs2]
    for vois in voisins2:
        parents[vois] = depart
        dfs2(G, vois)
    return parents

def Solution(end, parents):
    """
    Cette fonction sert a trouver le chemin entre la case de départ et la case d'arrivée.
    """
    chemin = []
    courant = end
    while courant != None:
        chemin = [courant] + chemin
        courant = parents[courant]
    return chemin


def cycle() :
    """
    Cette fonction dit si le labyrinthe possède ou non des cycles en se basant
    sur le résultat de la fonction isCyclic().
    """
    if isCyclic(map, (1,1)) == True:
        print("Le labyrinthe possède des cycles")
    else:
        print("Le labyrinthe est acyclique")
    menu()

def isCyclic(G,sommet):
    """
    Cette fonction se sert du dictionnaire parents pour détecter la présence de cycle
    au sein du labyrinthe.
    """
    sommets_visites=[]
    f=File()
    sommets_visites.append(sommet)
    f.enfiler((sommet,-1))
    while f.vide()==False:
        (tmp,parent)=f.defiler()
        voisins2=voisins(G,tmp)
        for vois in voisins2:
            if vois not in sommets_visites:
                sommets_visites.append(vois)
                f.enfiler((vois,tmp))
            elif vois!=parent:
                return True
    return False

#Enfin, on lance l'exécution du programme en appelant la fonction d'initialisation.
initialisation()