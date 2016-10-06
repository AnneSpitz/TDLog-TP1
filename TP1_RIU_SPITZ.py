#!/usr/bin/python
# -*- coding: utf-8 -*-

# /////////////////////////////////////////////////////
#
# TP1 du module de Techniques de Développement LOGiciel
#
# Groupe 3
# TP réalisé par RIU Clément et SPITZ Anne
#
# Rendu le Jeudi 06 Octobre 2016
#
# /////////////////////////////////////////////////////


from data import *


# Question 1 //////////////////////////////////////////////////////////////////////////////////////////////////////////
def creation_tableau_valeur(group_local, match_local):
    """
    Crée un tableau de tableaux de la forme : (nombre de points, nombre de buts marques, nombre de buts encaisses, pays).
    Prend en entrée l'ensemble des pays considérés et le tableau de la liste des matches.
    Renvoie un tableau de tableaux, les données étant triées en tenant compte des points, puis des différences de buts,
    puis du nombre de buts marqués, puis par ordre alphabétique.
    """

    tab_donnees_pays = []

    for pays in group_local:
        donnees_pays = [0, 0, 0, pays]

        for match in match_local:
            # On calcule le nombre de points
            if pays == match[0]:
                if match[1] > match[2]:
                    donnees_pays[0] += 2
                elif match[1] == match[2]:
                    donnees_pays[0] += 1

                donnees_pays[1] += match[1]
                donnees_pays[2] += match[2]

            elif pays == match[3]:
                if match[1] < match[2]:
                    donnees_pays[0] += 2
                elif match[1] == match[2]:
                    donnees_pays[0] += 1

                donnees_pays[1] += match[2]
                donnees_pays[2] += match[1]

        tab_donnees_pays.append(donnees_pays)

    return sorted(tab_donnees_pays, reverse=True)



def affiche_classement(group_local, match_local):
    """
    Permet d'afficher le classement des pays du groupe choisi.
    Prend en entrée l'ensemble des pays et le tableau des matchs.
    """

    taille_max = max([len(pays) for pays in group_local])

    tab_donnees_pays = creation_tableau_valeur(group_local, match_local)

    for points_pays in tab_donnees_pays:
        difference_buts = points_pays[1] - points_pays[2]

        print("{0:.<{width}} {1} pts {2}{3}".format(points_pays[3] + " ", points_pays[0], ["", "+"][difference_buts >= 0],
                                                    difference_buts, width=taille_max + 4))

    return None


# Question 2 //////////////////////////////////////////////////////////////////////////////////////////////////////////

def affiche_matches_joues(group_local, match_local):
    """
    Affiche les résultats des matchs d'un groupe.
    Prend en entrée un ensemble de pays et un tableau de matchs.
    """

    taille_max = max(len(match[0]) for match in match_local if match[0] in group_local)
    for match in match_local:
        if match[0] in group_local or match[3] in group_local:
            print("{0: <{width}} {1} - {2} {3}".format(*match, width=taille_max))

    return None


# Question 3 //////////////////////////////////////////////////////////////////////////////////////////////////////////

def verifie_match(group_local, match_local):
    """
    Renvoie une liste des couples de pays qui n'ont pas joué ensemble.
    Prend en entrée un ensemble de pays et un tableau de matchs.
    """

    group_de_travail = {pays for pays in group_local}
    match_restants = []

    for pays in group_local:
        group_de_travail.difference_update({pays})
        for pays2 in group_de_travail:
            match_existe = False
            for match in match_local:
                if (pays in match) and (pays2 in match):
                    match_existe = True
            if match_existe == False:
                match_restants.append((pays, pays2))

    return match_restants


def affiche_match_restants(group_local, match_local):
    """
    Affiche les matches restants.
    Prend en entrée un ensemble de pays et un tableau de matches.
    """

    match_restants = verifie_match(group_local, match_local)
    max_len_car_pays = max(len(match[0]) for match in match_restants)
    for match in match_restants:
        print("{0: <{width}} vs {1}".format(*match, width=max_len_car_pays))

    return None


# Question 4 //////////////////////////////////////////////////////////////////////////////////////////////////////////

def affiche_complet(numero_groupe):
    """
    Affiche l'ensemble des informations sur le groupe sélectionné.
    Prend en entrée la clef du groupe (ex :  "1" )
    """

    print("Group {0} \n--------".format(numero_groupe))
    affiche_classement(groups[numero_groupe], matches)
    print("")
    affiche_matches_joues(groups[numero_groupe], matches)
    print("")
    affiche_match_restants(groups[numero_groupe], matches)
    print("\n")

    return None


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Corps du programme :

print("Question 1 :")
affiche_classement(groups["1"], matches)
print("\n")

print("Question 2 :")
affiche_matches_joues(groups["1"], matches)
print("\n")

print("Question 3 :")
affiche_match_restants(groups["2"], matches)
print("\n")

print("Question 4 :")
affiche_complet("1")
affiche_complet("2")
