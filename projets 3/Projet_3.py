from typing import List, Tuple
from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog                      #On importe ce dont on a besoin
import matplotlib.pyplot as plt

def lirePoints(nomfichier):
    """Converti un fichier texte avec la syntaxe "x,y" 
    sur chaque ligne en une liste de tuple a deux arguments"""

    L = []
    with open(nomfichier, 'r') as file:
        try:
            n = int(file.readline().rstrip())       #on ouvre le fichier en lecture seul puisqu'on ne l'édite pas,
            for line in file.readlines():           #on sépare les deux nombres a l'emplacement de la virgule et on les ajoutent a L en tant que tuple
                x,y = line.rstrip().split(',')
                L.append((int(x),int(y)))
            return L
        except:                                     #si le fichier selectionné produit une quelconque erreur (syntaxe par exmple), le message suivant est affiché :
            showerror('Non valide',"Le fichier selectionné ne correspond pas a la syntaxe demandée.")
            return L

def Trier(S: List[Tuple]):
    """Tri une liste de tuple a deux argument dans l'ordre croissant,
     en fonction des deux éléments."""

    if S == []:                                                         #on vérifie que la liste n'est pas vide 
        return

    if type(S) != list or not all(type(x)==tuple for x in S):           #on revérifie la syntaxe, on ne sait jamais
        return "invalid argument"
    S.sort(key=lambda x:(x[0], x[1]))                                   #la commande de tri
    return S

def domine(p1: Tuple, p2: Tuple) -> bool:
    """Prend deux point et compare leur valeurs x et y. 
    renvoie True si p1 domine p2, False sinon."""  

    if type(p1)!=tuple or type(p2)!=tuple :         #syntaxe                      
        return "invalid argument"
    if  p1[0]>p2[0] and p1[1]>p2[1]:return True     #on vérifie x et y et on renvoie true ou false en conséquence

    else : return False

def taille(S:List[Tuple]) -> int :
    """Renvoie la taille d'une liste"""

    if type(S) != list : raise ValueError("S was not a list")           #syntaxe
    else : return len(S)                                                #on renvoie la longueur de la liste

def decouper(S:List[Tuple]) -> List: #Doit decouper S en SL et SR
    """découpe une liste en son milieu et en renvoie deux appelées 
    respectivement SL pour la partie de gauche et SR pour la partie de droite."""

    if type(S) != list : raise ValueError("S was not a list")           #syntaxe
    if len(S) <= 1: return S 
    m  =  len(S)//2                                                     #on calcule le milieu de la liste
    SL, SR  =  S[:m], S[m:]                                             #on créé SL et SR et on les renvoie
    return SL, SR


def ajouter(S:List[Tuple],p:Tuple) -> List :
    """Ajoute un élément dans une liste"""
    if not type(S) == list : raise ValueError("S was not a list")       #syntaxe
    if not type(p) == tuple : raise ValueError("p was not a tuple")
    S.append(p)                                                         #on ajoute
    return S                                                            #et on renvoie

'''fonction EPM'''
def EPM(points):
    """Fonction récurrente qui trouve le front de pareto d'une liste de point en se servant du diviser pour régner."""
    if taille(points) <= 1: return points           #on verifie la taille

    points = Trier(points)                          #on tri la liste 

    L,R = decouper(points)                          #on decoupe la liste en deux partie
    SL,SR = EPM(L), EPM(R)                          #résolution par recursivité

    t=min(SR)                                       #on definit t comme le point avec l'abcisse minimale de SR

    for point in SL : 
        if not domine(t,point): ajouter(SR, point)  #on ne rajoute a SR que les point du front gauche non dominés par t

    return SR

"""Partie graphique"""
main_window = Tk()

def graphique(): 
    x=[]
    y=[]
    print(pareto, 'longueur : ', taille(pareto))
    if listePoints !=  [] :                                        # on verifie si la liste de points n'est pas vide
      for Point in listePoints :
            plt.plot(Point[0],Point[1], marker="+", color="black") #affiche les points en noir 
    else: return  showinfo("Pas de Point", "Le fichier que vous avez séléctionné  ne contient pas de point") #si la liste est vide on envoie un message d'erreur
    for i in range(taille(pareto)):
        x.append(pareto[i][0])
        y.append(pareto[i][1])
    plt.plot(x, y, color="red")
    plt.plot(x, y,"k+")
    plt.show()                                                      #affiche le graphique 

def open_file():
    global listePoints, pareto

    open_file_path = filedialog.askopenfilename() #ouvre une fenettre windows pour ouvrir le ficher

    if open_file_path != "":                      
        if not open_file_path.endswith('.txt'):     #on verifie le format du fichier ici txt, si il ne l'est pas on affiche un message d'erreur
            showerror("Erreur de format","Le ficher selectionné n'est pas un fichier txt")
        else:
            print(open_file_path)
            listePoints = lirePoints(open_file_path) #initialisation de la liste de Point
            if listePoints != []:
                pareto = EPM(listePoints)              #Calcul du front de pareto
                print("front de pareto : ", pareto)
                main_window.withdraw()  
                graphique()                             #affichage du graphique 
                regenerate()                            #demande de regénération front de pareto après fermetur du graphique
    else:                                               #si pas de fichier ouvert ==> affichage d'un message d'erreur
      main_window.withdraw()     
      showerror('erreur', 'Veillez ouvrir un fichier')
      main_window.deiconify()

def regenerate():
    answer = askyesno("Continuer", "Voulez vous generer un autre front de pareto a partir d'un autre fichier ? ") #ouvre un dialog, pour continuer a générer des front de pareto
    if answer != True:                          #Si non on arrête le programme
      main_window.quit() 
      print("Arrêt confirmé")
    else:                                       # Si oui on reinitialise toutes les variable et on recommence l'ouverture du fichier
      global listePoints, pareto
      listePoints = []
      pareto = []
      open_file()

def quit():
    main_window.withdraw()                                              #on cache la fenetre principale
    question  = askyesno("Quitter","Etes vous sûr de vouloir quitter")  #ouverture dialoque de confirmation 
    if question != True:                                                #Si non on re affiche la fenetre principale
      main_window.deiconify()
    else: main_window.quit()                                            #Si oui, on quit le programme

"""fenetre principale"""
main_window.geometry("500x200") #taille de la fenetre principale
main_window.title("Calculateur de Front de pareto") #affectation d'un titre
main_text = Label(main_window,anchor=CENTER, text =  "Bienvenue dans le calculateur de  front de Pareto") #text
main_text.pack()
bouton=Button(main_window, text="Ouvrir un fichier txt depuis l'explorateur de fichier", command=open_file) #creation d'un boutton pour ouvrir les fichier
bouton.pack(padx=(20),pady=(20))
bouton_quit=Button(main_window, text="Quitter", command=quit) #creation d'un boutton pour quitter le programme
bouton_quit.pack(padx=(20),pady=(20))
main_window.mainloop() #affichage de la fenetre
