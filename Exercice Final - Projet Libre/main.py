from jeu import *
from affichage import *
from score import *

def main():
    score_actuel = initialiser_score()
    correspondance = {"1": "roche", "2": "papier", "3": "ciseaux"}

    while True:
        afficher_menu()
        choix = input("Entrez votre choix (1/2/3): ").strip()

        if choix not in correspondance:
            print("Choix invalide, veuillez réessayer.")
            continue

        choix_joueur = correspondance[choix]
        choix_ai = ai_choix()

        afficher_choix_joueur(choix_joueur)
        afficher_choix_ai(choix_ai)

        resultat = determiner_gagnant(choix_joueur, choix_ai)
        afficher_resultat(resultat)

        mettre_a_jour_score(resultat, score_actuel)
        afficher_score(score_actuel)

        reponse = input("Voulez-vous continuer à jouer ? (o/n): ").strip().lower()
        if reponse != "o":
            print("Merci d'avoir joué !")
            break

if __name__ == "__main__":
    main()
