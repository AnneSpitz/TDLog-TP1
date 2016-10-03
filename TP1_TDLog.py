# à faire : from data import

groups = {
    "1": {"Denmark", "England", "France", "Sweden"},
    "2": {"CIS", "Germany", "Netherlands", "Scotland"}
}

matches = [
    ("Sweden", 1, 1, "France"),
    ("Denmark", 0, 0, "England"),
    ("Netherlands", 1, 0, "Scotland"),
    ("CIS", 1, 1, "Germany"),
    ("France", 0, 0, "England"),
    ("Sweden", 1, 0, "Denmark"),
]


#Question 1


def rangement_donnees(pays_points):
    test = sorted(pays_points, key=lambda pays: (pays[1], pays[2], pays[3]), reverse=True)
    return test


#On crée un tableau de tuples de la forme (pays, nombre de points, nombre de buts marqués, nombre de buts encaissés)
def creation_tableau_valeur(group_local, match_local):
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

        pays_points.append((pays, nb_points, nb_buts_marques, nb_buts_encaisses))

    return pays_points


def affichage_classement_question_1(group_local, match_local):
    #à mettre en fonction externe
    taille_max = 0
    for pays in group_local:
        if len(pays) > taille_max:
            taille_max = len(pays)

    pays_points = creation_tableau_valeur(group_local, match_local)

    pays_points = rangement_donnees(pays_points)

    for i in range(len(pays_points)):
        taille_locale=taille_max-len(pays_points[i][0])
        difference_buts = pays_points[i][2]-pays_points[i][3]

        print(pays_points[i][0] + " " + "." * (taille_locale + 3) + " " + str(pays_points[i][1]) + " pts " + ["", "+"][difference_buts >= 0] + str(difference_buts))


affichage_classement_question_1(groups["1"], matches)


#Question 2
def affichage_matches_joués_question_2(group_local, match_local):
    #à mettre en fonction externe
    taille_max = 0
    for i in range(len(match_local)):
        if match_local[i][0] in group_local["1"] or match_local[i][3] in group_local["1"]:
            if len(match_local[i][0]) > taille_max:
                taille_max = len(match_local[i][0])
            if len(match_local[i][3]) > taille_max:
                taille_max = len(match_local[i][3])

    print("test")
    for i in range(len(match_local)):
        if match_local[i][0] in group_local["1"] or match_local[i][3] in group_local["1"]:
            taille_locale = taille_max - len(match_local[i][0])

            print(match_local[i][0] + " " + " " * (taille_locale) + str(match_local[i][1]) + " - " + str(match_local[i][2]) + " " + match_local[i][3])

affichage_matches_joués_question_2(groups, matches)


