import json
from ticket import Ticket



#Sauver les tickets
def sauvegarder_tickets(tickets):
    data = []
    for t in tickets:
        data.append({"id_ticket": t.id_ticket, "titre": t.titre, "description": t.description, "statut": t.statut})
    with open("tickets.json", "w") as f:
        json.dump(data, f)
    print("Tickets sauvegardés!")


def charger_tickets():
    try:
        with open("tickets.json", "r") as f:
            data = json.load(f)
            tickets = []
            for d in data:
                tickets.append(Ticket(d["id_ticket"], d["titre"], d["description"], d["statut"]))
            return tickets
    except FileNotFoundError:
        print("Aucun ticket sauvegarder en ce moment.")
        return []