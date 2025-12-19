#joueur 1 et ai store la str "roche","papier""ciseau"
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

