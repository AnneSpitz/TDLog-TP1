#!/usr/bin/python
# -*- coding: utf-8 -*-

from data import *


# groups = {
#     "1": {"Denmark", "England", "France", "Sweden"},
#     "2": {"CIS", "Germany", "Netherlands", "Scotland"}
# }
#
# matches = [
#     ("Sweden", 1, 1, "France"),
#     ("Denmark", 0, 0, "England"),
#     ("Netherlands", 1, 0, "Scotland"),
#     ("CIS", 1, 1, "Germany"),
#     ("France", 0, 0, "England"),
#     ("Sweden", 1, 0, "Denmark"),
# ]


# Question 1 //////////////////////////////////////////////////////////////////////////////////////////////////////////


def rangement_donnees(pays_points):
    """Renvoie les pays de la liste pays_points dans l'ordre de point, puis dans l'ordre de nombre de points d'avance,
    puis dans l'ordre de nombre de buts marqués, puis par ordre alphabétique. Prend une liste en entrée, renvoie une
    liste."""
    return sorted(pays_points, reverse=True)


def creation_tableau_valeur(group_local, match_local):
    """Crée un tableau de tuples de la forme (nombre de points, nombre de buts marques, nombre de buts encaisses, pays).
    Prend en entrée l'ensemble des pays considérés et le tableau de la liste des matches. Renvoie un tableau de tuples.
    """
    pays_points = []

    for pays in group_local:
        nb_points = 0
        nb_buts_marques = 0
        nb_buts_encaisses = 0

        for i in range(len(match_local)):
            # On calcule le nombre de points
            if pays == match_local[i][0]:
                if match_local[i][1] > match_local[i][2]:
                    nb_points += 2
                if match_local[i][1] == match_local[i][2]:
                    nb_points += 1

                nb_buts_marques += match_local[i][1]
                nb_buts_encaisses += match_local[i][2]

            if pays == match_local[i][3]:
                if match_local[i][1] < match_local[i][2]:
                    nb_points += 2
                if match_local[i][1] == match_local[i][2]:
                    nb_points += 1

                nb_buts_marques += match_local[i][2]
                nb_buts_encaisses += match_local[i][1]

        pays_points.append((nb_points, nb_buts_marques, nb_buts_encaisses, pays))

    return pays_points


def affichage_classement_question_1(group_local, match_local):
    """Permet d'afficher le classement selon la méthode définie par la fonction rangement_donnees. Prend en entrée
    l'ensemble des pays et le tableau des matchs."""
    # a mettre en fonction externe
    # taille_max = 0
    # for pays in group_local:
    #     if len(pays) > taille_max:
    #         taille_max = len(pays)

    taille_max = max([len(pays) for pays in group_local])

    pays_points = creation_tableau_valeur(group_local, match_local)

    pays_points = rangement_donnees(pays_points)

    for i in range(len(pays_points)):
        taille_locale = taille_max - len(pays_points[i][3])
        difference_buts = pays_points[i][1] - pays_points[i][2]

        print(pays_points[i][3] + " " + "." * (taille_locale + 3) + " " + str(pays_points[i][0]) + " pts " + ["", "+"][
            difference_buts >= 0] + str(difference_buts))


print("Question 1 :")
affichage_classement_question_1(groups["1"], matches)
print("\n")

# Question 2 //////////////////////////////////////////////////////////////////////////////////////////////////////////
def affichage_matches_joues_question_2(group_local, match_local):
    """Affiche les résultats des matchs d'un groupe. Prend en entrée un ensemble de pays et un tableau de matchs."""
    # a mettre en fonction externe
    taille_max = 0
    for i in range(len(match_local)):
        if match_local[i][0] in group_local or match_local[i][3] in group_local:
            if len(match_local[i][0]) > taille_max:
                taille_max = len(match_local[i][0])
            if len(match_local[i][3]) > taille_max:
                taille_max = len(match_local[i][3])

    for i in range(len(match_local)):
        if match_local[i][0] in group_local or match_local[i][3] in group_local:
            taille_locale = taille_max - len(match_local[i][0])

            print(match_local[i][0] + " " + " " * (taille_locale) + str(match_local[i][1]) + " - " + str(
                match_local[i][2]) + " " + match_local[i][3])


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
            if pays2 != pays :
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
        print("{0} {1} vs {2}".format(match[0], " " * (max_len_car_pays - len(match[0])), match[1]))


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