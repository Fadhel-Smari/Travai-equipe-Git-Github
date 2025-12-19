import ticket

def changer_statut():
        titre = input("Titre du ticket a modifier: ")

        if titre in tickets:
                print("1. À faire\n2. En Cours\n3. Terminer")
                choix = input("Nouveau statu(1-3): ")

                if choix == "1":
                        ticket[titre].statut = "À faire"
                elif choix == "2":
                        ticket[titre].statut = "En Cours"
                elif choix == "3":
                        ticket[titre].statut = "Terminer"

                print(f"Statut de {titre} changé à: {ticket[titre].statut}")
        return tickets