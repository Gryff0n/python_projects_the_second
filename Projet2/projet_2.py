"""IMPORTANT : pour faciliter la correction, les commandes qui affichent les résultat sont mises en commentaire,
 vous n'avez qu'a aller au 'a faire vous meme' que vous souhaiter et enlever les guillemets avant d'executer le programme."""


#----------------------------------I) CONSTRUCTION ET REPRESENTATION D’ARBRES :

class ArbreBinaire:
    def __init__(self, valeur):
        self.valeur = valeur
        self.enfant_gauche = None
        self.enfant_droit = None
    def insert_gauche(self, valeur):
        if self.enfant_gauche == None:
            self.enfant_gauche = ArbreBinaire(valeur)
        else:
            new_node = ArbreBinaire(valeur)
            new_node.enfant_gauche = self.enfant_gauche
            self.enfant_gauche = new_node
    def insert_droit(self, valeur):
        if self.enfant_droit == None:
            self.enfant_droit = ArbreBinaire(valeur)
        else:
            new_node = ArbreBinaire(valeur)
            new_node.enfant_droit = self.enfant_droit
            self.enfant_droit = new_node
    def get_valeur(self):
        return self.valeur
    def get_gauche(self):
        return self.enfant_gauche
    def get_droit(self):
        return self.enfant_droit
    def estFeuille(self):
        if not self.enfant_gauche and not self.enfant_droit:
            return True
        else:
            return False
#######fin de la classe########

######début de la construction de l'arbre binaire###########
racine = ArbreBinaire('A')
racine.insert_gauche('B')
racine.insert_droit('F')
b_node = racine.get_gauche()
b_node.insert_gauche('C')
b_node.insert_droit('D')
f_node = racine.get_droit()
f_node.insert_gauche('G')
f_node.insert_droit('H')
c_node = b_node.get_gauche()
c_node.insert_droit('E')
g_node = f_node.get_gauche()
g_node.insert_gauche('I')
h_node = f_node.get_droit()
h_node.insert_droit('J')
######fin de la construction de l'arbre binaire###########

# =============================================================================
# Représentation graphique
# =============================================================================

from tkinter import *
from math import *

# ------------------- cercle-------------------#
def cercle(canv,x,y,r,col,colf):
    """dessine un cercle graphique sur le canvas de centre (x,y) de rayon r de
    couleur col et de couleur de fond colf"""
    canv.create_oval(x-r,y-r,x+r,y+r,outline=col, fill=colf)
# ------------------- dessinenoeud-------------------#
def dessinenoeud(canv,x,y,r,noeud):
    """ dessine un noeud graphique : un cercle rempli avec la valeur du noeud"""
    cercle(canv,x,y,r,"black","white")
    canv.create_text(x,y,text=noeud.valeur,fill="black")
# ------------------- centresuivant-------------------#
def centresuivant(x,y,r,m,dir,ouverture):
    # ouverture permet d'ajuster l'angle d'ouverture des noeuds
    """ calcule la position de noeud suivant :
    on calcule a et b les décalages par rapport à la position actuelle x,y
    dir permet de spécifier:
    si c'est un fils gauche on retranche le a
    si c'est un fils droit on ajoute le a à x
    pour y on ajoute toujours b dans les deux cas.
    m la distance entre les cercles : le nœud et ses descendants.
    """
    a=(2*r+m)*sin(pi/(ouverture)) # calcule le décalage sur l'axe des x : coordonnées polaire vers
    # cordonnées cartésiennes
    b=(2*r+m)*cos(pi/(ouverture)) # de même pour le décalage sur y. l'angle d'ouverture est 45 ° pour ouverture = 4
    if dir=="l": # dir pour left ou right c.à.d. fils gauche ou fils droit
        x1,y1=x-a,y+b # on décale vers la gauche donc on retranche a de x et
    # on ajoute b à y on descend vers le bas
    else:
        x1,y1=x+a,y+b # on décale vers la droite donc on ajoute a à x
    ouverture += 3 # en augmentant ouverture, on diminue l'angle pour la ligne suivante
    return x1,y1,ouverture
    # ------------------- tracearbre-------------------#
def tracearbre(canv,x,y,r,m,noeud,ouverture):
    """ trace l'arbre graphique récursivement"""
    pas = 40 # pas ajustable permettant de réduire la distance entre les noeuds
    # pour éviter que des noeuds se superposent
    if noeud.estFeuille()==False: # si le noeud n'est pas une feuille
        if noeud.enfant_droit==None and noeud.enfant_gauche!=None : # s'il a un fils gauche mais pas de fils droit
            x1,y1,ouverture=centresuivant(x,y,r,m,"l",ouverture) # récupération de la position du noeud fils
            canv.create_line(x,y,x1,y1,fill="black") # tracé d'une droite entre x,y et x1,y1
            # cette fonction est dans la bibilothèque tkinter
            tracearbre(canv,x1,y1,r,m-pas,noeud.enfant_gauche,ouverture) # appel récursif pour traiter ce fils
        elif noeud.enfant_droit!=None and noeud.enfant_gauche==None : # s'il a un fils droit mais pas de fils gauche
            x1,y1,ouverture=centresuivant(x,y,r,m,"r",ouverture) # récupération de la position du noeud fils
            canv.create_line(x,y,x1,y1,fill="black") # tracé d'une droite entre x,y et x1,y1
            tracearbre(canv,x1,y1,r,m-pas,noeud.enfant_droit,ouverture) # appel récursif pour traiter ce fils
        else: # si il a un fils gauche et un fils droit
            x1,y1,ouverture=centresuivant(x,y,r,m,"l",ouverture) # récupération de la position du noeud fils gauche
            canv.create_line(x,y,x1,y1,fill="black") # tracé d'une droite entre x,y et x1,y1
            tracearbre(canv,x1,y1,r,m-pas,noeud.enfant_gauche,ouverture) # appel récursif pour traiter ce fils gauche
            x1,y1,ouverture=centresuivant(x,y,r,m,"r",ouverture-3) # récupération de la position du noeud fils droit
            # ouverture-3 pour compenser sur le noeud de droite
            # le +=3 dans centresuivant déjà appliqué
            canv.create_line(x,y,x1,y1,fill="black") # tracé d'une droite entre x,y et x1,y1
            tracearbre(canv,x1,y1,r,m-pas,noeud.enfant_droit,ouverture) # appel récursif pour traiter ce fils droit
    dessinenoeud(canv,x,y,r,noeud) # tracé du noeud courant
# ------------------- graphicarbre-------------------#
def graphicarbre(noeud):
    """ fonction de tracé graphique d'un arbre """
    cwidth=1000 # la largeur du canvas graphique
    cheight=700 # la hauteur du canvas
    couleurs=["red","green","bleu","white","black","cyan","magenta","yellow"]
    # fen est l'objet fenêtre héritée de la bibliothèque tkinter
    fen=Tk()
    # création d'un bouton avec la commande fermer(quit) attachée à la fenêtre
    btn=Button(fen, text="Quitter",command=fen.destroy)
    # placement du bouton en bas de la fenêtre
    btn.pack(side="bottom")
    # création d'un panneau dans lequel on affichera l'arbre
    pan=LabelFrame(fen)
    # placement de ce panneau en faut de la fenêtre
    pan.pack(side="top")
    # creation du canva graphique dans ce panneau
    canv=Canvas(pan,width=cwidth,height=cheight)
    # placement de ce canva en haut du panneau graphique
    canv.pack(side="top")
    # appel de la fonction de tracé graphique de l'arbre créé ci haut
    tracearbre(canv,cwidth//2,100,12,200,noeud,3)
    # actualisation de l'affichage graphique
    fen.mainloop()

#a faire vous meme 3
graphicarbre(racine)


#A faire vous meme 4

racine = ArbreBinaire('A')
racine.insert_gauche('B')
racine.insert_droit('C')
b_node = racine.get_gauche()
b_node.insert_gauche('D')
b_node.insert_droit('E')

graphicarbre(racine)


#------------------------------------------------II) HAUTEUR ET TAILLE D’UN ARBRE

"""a faire vous meme 5

HAUTEUR :
    Si T=NIL :
        renvoyer 0
    Sinon :
        renvoyer 1 + MAX(HAUTEUR(T.fils_gauche), HAUTEUR(T.fils_droit))
"""
def hauteur(T) :
    if T == None :
        return 0
    else :
        return 1 + max(hauteur(T.get_gauche()), hauteur(T.get_droit()))

print(hauteur(racine))

"""a faire vous meme 6

TAILLE :
    Si T=NIL :
        renvoyer 0
    Sinon :
        renvoyer 1 + TAILLE(T.fils_gauche) + TAILLE(T.fils_droit)
"""
def taille(T) :
    if T==None :
        return 0
    else :
        return 1 + taille(T.get_gauche()) + taille(T.get_droit())

print(taille(racine))

#-----------------------------------------------------III) PARCOURS D’UN ARBRE :

"""À faire vous-même 7

PARCOURS-INFIXE(T) :
    si T ≠ NIL :
        x ← T.racine
        PARCOURS-INFIXE(x.gauche)
        affiche x.clé
        PARCOURS-INFIXE(x.droit)
"""

def parcours_infixe(T):
    if not T == None:
        x = T
        if not parcours_infixe(x.get_gauche()) == None:
            print(parcours_infixe(x.get_gauche()))
        print(x.get_valeur())
        if not parcours_infixe(x.get_droit()) == None: 
            print(parcours_infixe(x.get_droit()))
    else: 
        return

parcours_infixe(racine)

"""
a faire vous meme 8

PARCOURS-PREFIXE(T) :
    si T ≠ NIL :
        x ← T.racine
        affiche x.clé
        PARCOURS-PREFIXE(x.gauche)
        PARCOURS-PREFIXE(x.droit)
"""   

def parcours_prefixe(T):
    if not T == None:
        x = T
        print(x.get_valeur())
        if not parcours_prefixe(x.get_gauche()) == None: 
            print(parcours_prefixe(x.get_gauche()))
        if not parcours_prefixe(x.get_droit()) == None: 
            print(parcours_prefixe(x.get_droit()))
    else: 
        return 

parcours_prefixe(racine)

"""
a faire vous meme 9

PARCOURS-SUFFIXE(T) :
    si T ≠ NIL :
        x ← T.racine
        PARCOURS-PREFIXE(x.gauche)
        PARCOURS-PREFIXE(x.droit)
        affiche x.clé
"""   

def parcours_suffixe(T):
    if not T == None:
        x = T
        if not parcours_suffixe(x.get_gauche()) == None: 
            print(parcours_suffixe(x.get_gauche()))
        if not parcours_suffixe(x.get_droit()) == None: 
            print(parcours_suffixe(x.get_droit()))
        print(x.get_valeur())
    else: 
        return 

parcours_suffixe(racine)

"""
a faire vous meme 10

PARCOURS-LARGEUR(T) :
    enfiler(T.racine, f)
    tant que f n'est pas vide :
        x ← defiler(f)
        afficher x.clé
        si x.gauche ≠ NIL :
            Tg ← x.gauche
            enfiler(Tg.racine, f)
        si x.droit ≠ NIL :
            Td ← x.droite
            enfiler(Td.racine, f)
"""
#On utilise une classe file du cours pour nous faciliter la tache :
class File:
    ''' classe File
    création d'une instance File avec une liste
    '''
    def __init__(self):
        "Initialisation d'une file vide"
        self.L = []
    def vide(self):
        "teste si la file est vide"
        return self.L == []
    def defiler(self):
        "défile"
        assert not self.vide(), "File vide"
        return self.L.pop(0)
    def enfiler(self,x):
        "enfile"
        self.L.append(x)

def parcours_largeur(T):
    f = File()
    f.enfiler(T)
    while not f.vide() == True:
        x = f.defiler()
        print(x.get_valeur())
        if not x.get_gauche() == None:
            Tg = x.get_gauche()
            f.enfiler(Tg)
        if not x.get_droit() == None:
            Td = x.get_droit()
            f.enfiler(Td)
    return

parcours_largeur(racine)

#-----------------------------------------IV) LES ARBRES BINAIRES DE RECHERCHE :

#création de l'arbre :

"""a faire vous meme 11"""

racine = ArbreBinaire(15)
racine.insert_gauche(6)
racine.insert_droit(18)
node_6 = racine.get_gauche()
node_6.insert_gauche(3)
node_6.insert_droit(7)
node_18 = racine.get_droit()
node_18.insert_gauche(17)
node_18.insert_droit(20)
node_3 = node_6.get_gauche()
node_3.insert_gauche(2)
node_3.insert_droit(4)
node_7 = node_6.get_droit()
node_7.insert_droit(13)
node_13 = node_7.get_droit()
node_13.insert_gauche(9)

graphicarbre(racine)

"""a faire vous meme 12"""
parcours_infixe(racine)
#On peut en conclure qu'il s'agit d'un arbre binaire de recherche car le parcours infixe renvoie l'arbre dans l'ordre croissant.

'''
a faire vous meme 13

ARBRE-RECHERCHE(T,k) :
    si T == NIL :
        renvoyer faux
    x ← T.racine
    si k == x.clé :
        renvoyer vrai
    si k < x.clé :
        renvoyer ARBRE-RECHERCHE(x.gauche, k)
    sinon :
        renvoyer ARBRE-RECHERCHE(x.droit, k)
'''

def arbre_recherche(T, k):
    if T == None: 
        return False
    x = T
    if k == x.get_valeur(): 
        return True
    if k < x.get_valeur(): 
        return arbre_recherche(x.get_gauche(), k)
    else: 
        return arbre_recherche(x.get_droit(), k)

print("k = 13 : ",arbre_recherche(racine, 13))
print("k = 16 : ",arbre_recherche(racine, 16)) 

"""
a faire vous meme 14

ARBRE-RECHERCHE_ITE(T,k) :
  x ← T.racine
  tant que T ≠ NIL et k ≠ x.clé :
    x ← T.racine
    si k < x.clé :
      T ← x.gauche
    sinon :
      T ← x.droit
  si k == x.clé :
    renvoyer vrai
  sinon :
    renvoyer faux
"""

def arbre_recherche_ite(T,k):
  x = T
  while T != None and k != x.get_valeur():
    x = T
    if k < x.get_valeur(): 
        T = x.get_gauche()
    else: 
        T = x.get_droit()
  if k == x.get_valeur(): 
    return True
  else: 
    return False

print("k = 13 : ",arbre_recherche_ite(racine, 13))
print("k = 16 : ",arbre_recherche_ite(racine, 16)) 

"""
a faire vous meme 15

ARBRE-INSERTION(T, y) :
    x ← T.racine
    tant que T ≠ NIL :
        x ← T.racine
        si y.clé < x.clé :
            T ← x.gauche
        sinon :
            T ← x.droit
    si y.clé < x.clé :
        x.inserer_gauche y
    sinon :
        x.inserer_droite y
"""

def arbre_insertion(T, y):
    x = T
    while T != None:
        x = T
        if y < x.get_valeur(): 
            T = x.get_gauche()
        else: 
            T = x.get_droit()
    if y < x.get_valeur(): 
        x.insert_gauche(y)
    else: 
        x.insert_droit(y)

arbre_insertion(racine, 16)
#on affiche le nouvel arbre
graphicarbre(racine) 