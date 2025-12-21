import gestion
import ticket
import sauvegarde


def main():
    tickets = {t.id_ticket: t for t in sauvegarde.charger_tickets()}

    while True:
        requete = input(
            "1 - Ajouter un ticket\n"
            "2 - Modifier le statut d’un ticket\n"
            "3 - Quitter l’application\n"
            "Choix : "
        )

        match requete:
            case "1":
                tickets = gestion.ajouter_ticket(tickets)
            case "2":
                tickets = gestion.changer_statut(tickets)
            case "3":
                sauvegarde.sauvegarder_tickets(tickets.values())
                print("Application fermée.")
                break
            case _:
                print("Choix invalide, veuillez réessayer.")

    print("\nListe des tickets :")
    for t in tickets.values():
        print(f"[{t.id_ticket}] | {t.titre} | {t.statut}")


main()
