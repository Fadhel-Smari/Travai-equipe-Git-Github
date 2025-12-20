# Cette classe représente un ticket.
# Contient l'ID, le titre, la description.

class Ticket:
    def __init__(self, id_ticket, titre, description, statut):
        self.id_ticket = id_ticket
        self.titre = titre
        self.description = description
        self.statut = statut
