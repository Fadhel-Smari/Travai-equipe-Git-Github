
def afficher_desserts():
    desserts = ["Mochi Ice Cream", "Kheer", "Tiramisu"]
    print("=== DESSERTS ===")
    for d in desserts:
        print(d)
   

def main():
    print("=== MENU DU RESTAURANT ===")
    afficher_entrees()
    afficher_plats_principaux()
    afficher_desserts()


if __name__ == "__main__":
    main()