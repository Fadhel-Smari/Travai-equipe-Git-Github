import gestion
import ticket
import sauvegarde

def main():

    tickets = {t.id_ticket: t for t in sauvegarde.charger_tickets()}

    while True:
        requete = input("1 - ajout de ticket\n2 - changer statut\n3 - quitter\n ")

        match requete:
            case "1":
                tickets = gestion.ajouter_ticket(tickets)
            case "2":
                tickets = gestion.changer_statut(tickets)
            case "3":
                sauvegarde.sauvegarder_tickets(tickets.values())
                break
    
    for t in tickets.values():
        print(f"{t.id_ticket} -  {t.titre} - {t.description} - {t.statut}")
main() 