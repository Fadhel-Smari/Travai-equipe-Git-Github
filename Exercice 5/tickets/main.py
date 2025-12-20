import gestion
import ticket

def main():

    tickets = {}

    while True:
        requete = input("1 ajout de ticket, 2 changer statut ,3 quitter: ")

        match requete:
            case "1":
                tickets = gestion.ajouter_ticket(tickets)
            case "2":
                tickets = gestion.changer_statut(tickets)
            case "3":
                break
    
    for titre, t in tickets.items():
        print(f"{titre}: {t.id_ticket}, {t.description}, {t.statut}")
main()