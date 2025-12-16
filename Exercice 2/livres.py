
bibliotheque = []

# Fonction pour ajouter un livre à la bibliothèque
def ajouter_livre(titre, auteur):
    livre = {"titre": titre, "auteur": auteur}
    bibliotheque.append(livre)

def afficher_livres():
    for livre in bibliotheque:
        print(f"{livre['titre']} - {livre['auteur']}")

def rechercher_livre(titre):
    pass