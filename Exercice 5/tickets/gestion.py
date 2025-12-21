import ticket


def ajouter_ticket(tickets):
        if not tickets:
                id_ticket = 1
        else:
                id_ticket = max(tickets.keys()) + 1
        titre = input("Titre du ticket: ")
        description = input("Description du ticket: ")
        statut = "À faire"
        nouveau_ticket = ticket.Ticket(id_ticket, titre, description, statut)
        tickets[id_ticket] = nouveau_ticket
        print(f"Ajout de: - id: {nouveau_ticket.id_ticket} - titre: {nouveau_ticket.titre} - desc.: {nouveau_ticket.description} - statut: {nouveau_ticket.statut}")
        return tickets

def changer_statut(tickets):
        id = int(input("Id du ticket a modifier: "))

        if id in tickets:
                print("1. À faire\n2. En Cours\n3. Terminer\n")
                choix = input("Nouveau statu(1-3): ")

                if choix == "1":
                        tickets[id].statut = "À faire"
                elif choix == "2":
                        tickets[id].statut = "En Cours"
                elif choix == "3":
                        tickets[id].statut = "Terminer"

                print(f"Statut de {id} changé à: {tickets[id].statut}")
        return tickets
