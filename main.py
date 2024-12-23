#### Imports et définition des variables globales
#import random
"""
On utilise les fonctions secondaire pour lire une ligne du fichier et d'en extraire les nombres
pour en obtenir, son minimum, son maximum, le dernier nombre, le premier 
"""

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename,mode='r', encoding='utf8') as file:
        l=file.readlines()
        tableau=[]
        for i in range (len(l)):
            li=[int(x) for x in l[i][:-1].split(";")]
            tableau.append(li)
    return tableau

def get_list_k(data, k):
    """On retourne l'indice qui se trouve en k"""
    return data[k]

def get_first(l):
    """On renvoie la première valeur de la ligne passée en paramètre"""
    #listeC=l.split(';')
    #firstI = int(listeC[0])
    return int(l[0])

def get_last(l):
    """On renvoie la dernière valeur de la ligne passée en paramètre"""
    #listeC=l[:-1].split(';')
    #lastI = int(listeC[-1])
    return int(l[-1])

def get_max(l):
    """On renvoie la valeur maximum de la ligne passée en paramètre"""
    # listeC=l[:-1].split(';')
    #listeI = [int(x) for x in listeC]
    maxi= max(l)
    return int(maxi)

def get_min(l):
    """On renvoie la valeur minimum de la ligne passée en paramètre"""
    #=l[:-1].split(';')
    #listeI = [int(x) for x in listeC]
    mini= min(l)
    return int(mini)

def get_sum(l):
    """On renvoie la somme des valeurs de la ligne passée en paramètre"""
    #listeC=l[:-1].split(';')
    #listeI = [int(x) for x in listeC]
    sumi= sum(l)
    return int(sumi)


#### Fonction principale


def main():
    """On fait quelques appels aux fonctions secondaires dans le main"""
    l = read_data(FILENAME)
    get_max(l[10])
    get_min(l[4])
    get_sum(l[5])
    get_first(l[0])
    get_last(l[3])
    # data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
