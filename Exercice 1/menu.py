# ajouts des entrées
def afficher_entrees():
    liste_entrees = ["soupe aux légumes", "salade césar", "6 aile de poulet"]
    print("\n=== ENTRÉES ===")
    for entree in liste_entrees:
        print(entree)

# ajouts des désserts
def afficher_desserts():
    desserts = ["Mochi Ice Cream", "Kheer", "Tiramisu"]
    print("=== DESSERTS ===")
    for d in desserts:
        print(d)
   

# Structure de départ
def main():
    print("=== MENU DU RESTAURANT ===")
    afficher_entrees()
    afficher_plats_principaux()
    afficher_desserts()

    # Les autres ajouteront leur code ici


if __name__ == "__main__":
    main()