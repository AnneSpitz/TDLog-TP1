#!/usr/bin/python
# -*- coding: utf-8 -*-

from data import *


# Question 1 //////////////////////////////////////////////////////////////////////////////////////////////////////////


def rangement_donnees(pays_points):
    """Renvoie les pays de la liste pays_points dans l'ordre de point, puis dans l'ordre de nombre de points d'avance,
    puis dans l'ordre de nombre de buts marqués, puis par ordre alphabétique. Prend une liste en entrée, renvoie une
    liste."""
    return sorted(pays_points, reverse=True)


def creation_tableau_valeur(group_local, match_local):
    """Crée un tableau de tuples de la forme (nombre de points, nombre de buts marques, nombre de buts encaisses, pays).
    Prend en entrée l'ensemble des pays considérés et le tableau de la liste des matches. Renvoie un tableau de tableau.
    """
    pays_points = []

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

            if pays == match[3]:
                if match[1] < match[2]:
                    donnees_pays[0] += 2
                elif match[1] == match[2]:
                    donnees_pays[0] += 1

                donnees_pays[1] += match[2]
                donnees_pays[2] += match[1]

        pays_points.append(donnees_pays)

    return pays_points


def affichage_classement_question_1(group_local, match_local):
    """Permet d'afficher le classement selon la méthode définie par la fonction rangement_donnees. Prend en entrée
    l'ensemble des pays et le tableau des matchs."""
    taille_max = max([len(pays) for pays in group_local])

    pays_points = creation_tableau_valeur(group_local, match_local)

    pays_points = rangement_donnees(pays_points)

    for points_pays in pays_points:
        taille_locale = taille_max - len(points_pays[3])
        difference_buts = points_pays[1] - points_pays[2]

        print("{0} {1} {2} pts {3}{4}".format(points_pays[3], "." * (taille_locale + 3), str(points_pays[0]),
                                              ["", "+"][difference_buts >= 0], str(difference_buts)))


print("Question 1 :")
affichage_classement_question_1(groups["1"], matches)
print("\n")


# Question 2 //////////////////////////////////////////////////////////////////////////////////////////////////////////
def affichage_matches_joues_question_2(group_local, match_local):
    """Affiche les résultats des matchs d'un groupe. Prend en entrée un ensemble de pays et un tableau de matchs."""

    taille_max = max(len(match[0]) for match in match_local if match[0] in group_local)
    for match in match_local:
        if match[0] in group_local or match[3] in group_local:
            print("{: <{width}} {} - {} {}".format(*match, width=taille_max))


print("Question 2 :")
affichage_matches_joues_question_2(groups["1"], matches)
print("\n")


# Question 3 //////////////////////////////////////////////////////////////////////////////////////////////////////////

def verifie_match(group_local, match_local):
    """Renvoie une liste de couple de pays qui n'ont pas joué de match ensemble. Prend en entrée un ensemble de pays et
    un tableau de matchs."""
    group_travail = {pays for pays in group_local}
    match_non_fait = []
    for pays in group_local:
        group_travail.difference_update({pays})
        for pays2 in group_travail:
            match_existe = False
            for match in match_local:
                if (pays in match) and (pays2 in match):
                    match_existe = True
            if match_existe == False:
                match_non_fait.append((pays, pays2))
    return match_non_fait


def affiche_match_non_fait_question_3(group_local, match_local):
    """Affiche les matchs non encore fait. Prend en entrée un ensemble de pays et un tableau de matchs."""
    match_non_fait = verifie_match(group_local, match_local)
    max_len_car_pays = max(len(match[0]) for match in match_non_fait)
    for match in match_non_fait:
        print("{0} {1}vs {2}".format(match[0], " " * (max_len_car_pays - len(match[0])), match[1]))


print("Question 3 :")
affiche_match_non_fait_question_3(groups["2"], matches)
print("\n")

# Question 4 //////////////////////////////////////////////////////////////////////////////////////////////////////////

print("Question 4 :")
numero_groupe = "1"
print("Group {0} \n--------".format(numero_groupe))
affichage_classement_question_1(groups[numero_groupe], matches)
print("")
affichage_matches_joues_question_2(groups[numero_groupe], matches)
print("")
affiche_match_non_fait_question_3(groups[numero_groupe], matches)
print("\n")

numero_groupe = "2"
print("Group {0} \n --------".format(numero_groupe))
affichage_classement_question_1(groups[numero_groupe], matches)
print("")
affichage_matches_joues_question_2(groups[numero_groupe], matches)
print("")
affiche_match_non_fait_question_3(groups[numero_groupe], matches)
print("\n")
