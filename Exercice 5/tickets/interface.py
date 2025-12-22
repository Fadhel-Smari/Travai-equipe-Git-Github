# Interface utilisateur

def afficher_liste_tickets(tickets):
    
    print("\n" + "="*30)
    print("      LISTE DES TICKETS")
    print("="*30)
    
    if not tickets:
        print("Aucun ticket à afficher.")
    else:
        for t in tickets.values():
            # Formatage : [ID] | Titre | STATUT
            print(f"[{t.id_ticket}] | {t.titre} | {t.statut}")
    
    print("="*30 + "\n")