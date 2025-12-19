def afficher_menu():
    print("Bienvnue au jeu de roche papier et ciseaux")
    print("1- Roche")
    print("2 - Papier")
    print("ciseau")

    print("Vous etes joueur1")

def afficher_choix_joueur(choix_joueur):
    print(f"vous avex choisi: {choix_joueur}")

def afficher_choix_ai(choix_ordi):
    print(f"Ai a choisi: {choix_ordi}")

def afficher_resultat(resultat):
    if resultat == "gagné":
        print("Bravo! Vous avez gagne!")
    elif resultat == "perdu":
        print("Vous avez perdu.")
    else:
        print("Match nul.")