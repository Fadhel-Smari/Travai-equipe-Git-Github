# Importe tous les modules et orchestre le jeu
from mots import choisir_mot
from affichage import afficher_pendu
from jeu import jouer_tour

def main():
    print("===Jeu du Pendu ===")

    mot_secret = choisir_mot()
    lettres_trouvees = []
    erreurs = 0
    max_erreurs = 6
    mot_complet = False
    while erreurs < max_erreurs:
        afficher_pendu(erreurs)

        mot_affiche = ""
        mot_complet = True
        for lettre in mot_secret:
            if lettre in lettres_trouvees:
                mot_affiche += lettre
            else:
                mot_affiche += "_"
                mot_complet = False
        print(mot_affiche)

        if mot_complet:
            break

        #Demander une lettre
        lettre = input("Devinez une lettre du mot: ")

        lettres_trouvees, erreurs = jouer_tour(mot_secret, lettres_trouvees, lettre)

    afficher_pendu(erreurs)
    print(mot_affiche)

    if mot_complet:
        print("Bravo! Vous avez bien deviné le mot")
    else:
        print("Oops! Vous avez perdu.")

main()