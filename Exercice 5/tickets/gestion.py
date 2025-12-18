import sauvegarde
tickets = []

def ajouter_ticket():
        nouveau_ticket = input("Ticket a ajouter: ")
        tickets.append(nouveau_ticket)
        return tickets

def supprimer_ticket():
        ticket_supprimer = input("Ticket a enlevé:")
        tickets.remove(ticket_supprimer)
        return tickets




