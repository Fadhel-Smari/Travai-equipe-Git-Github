import random

# Fonction pour retourne un mot aléatoire de la liste
def choisir_mot():
    mots = ["python", "programmation", "github", "collaboration"]
    mot_aleatoire = random.choice(mots)
    return mot_aleatoire