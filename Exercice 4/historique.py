def sauvegarder_calcul(nom, imc):
    
    # Sauvegarde dans un fichier
    nom_final = nom if nom else "Anonyme"
    with open(FICHIER_HISTORIQUE, "a", encoding="utf-8") as f:
        f.write(f"{nom_final};{imc:.2f}\n")

def afficher_historique():

    # Lit le fichier
    try:
        with open(FICHIER_HISTORIQUE, "r", encoding="utf-8") as f:
            lignes = f.readlines()
            
        if not lignes:
            print("L'historique est vide.")
            return

        print("\n=== Historique des IMC ===")
        for i, ligne in enumerate(lignes, start=1):
            if ";" in ligne:
                nom, val = ligne.strip().split(";")
                print(f"{i}. {nom} -> IMC: {val}")
    except FileNotFoundError:
        print("Aucun fichier d'historique trouvé.")