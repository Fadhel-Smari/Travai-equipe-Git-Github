def initialiser_score():
 
    return {"joueur": 0, "ai": 0}
 
def mettre_a_jour_score(resultat, score):
 
    if resultat == "gagné":
        score["joueur"] += 1
    elif resultat == "perdu":
        score["ai"] += 1
    return score
 
def afficher_score(score):
 
    print(f"Score - Joueur: {score['joueur']} | AI: {score['ai']}")
 