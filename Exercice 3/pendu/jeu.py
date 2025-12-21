def jouer_tour(mot_secret, lettres_trouvees, lettre):
    pass
    # Logique du jeu
    lettre = lettre.lower()
    
    # Si la lettre est déjà deviné
    if lettre in lettres_trouvees:
        print(f"Vous avez déjà deviné la lettre '{lettre}'.")
        return lettres_trouvees, 0 

    # Si la lettre est dans le mot
    if lettre in mot_secret:
        lettres_trouvees.append(lettre)
        return lettres_trouvees, 0 
    else:
        # Aucune lettre du mot
        print(f"La lettre '{lettre}' n'est pas dans le mot.")
        return lettres_trouvees, 1 # mauvaise lettre