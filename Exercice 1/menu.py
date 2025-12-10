# Structure de départ
def main():
    print("=== MENU DU RESTAURANT ===")
    # Les autres ajouteront leur code ici

    #ajouts des entrées
    def afficher_entrees():
        liste_entrees = ["soupe aux légumes", "salade césar", "6 aile de poulet"]
        print("\n=ENTRÉES=")
        for entree in liste_entrees:
            print(entree)
    afficher_entrees()


if __name__ == "__main__":
    main()