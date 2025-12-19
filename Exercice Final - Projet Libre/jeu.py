import random

def ai_choix():
    option = ["roche", "papier", "ciseaux"]
    ai = random.choice(option)
    return ai

#joueur 1 et ai store la str "roche","papier""ciseau" et compare si gagnant ou non
def determiner_gagnant(joueur1, ai):
    if joueur1 == ai:
        return "match nul"
    match joueur1:
        case "roche":
            if ai == "ciseaux":
                return "gagné"
            else:
                return "perdu"
        case "papier":
            if ai == "roche":
                return "gagné"
            else:
                return "perdu"
        case "ciseaux":
            if ai == "papier":
                return "gagné"
            else:
                return "perdu"

