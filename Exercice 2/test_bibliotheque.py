from livres import ajouter_livre, afficher_livres, rechercher_livre

#ajouter un livre
ajouter_livre('1984', 'George Orwell')

#test d'affichage
print("Test d'affichage de livres")
afficher_livres()

#test de recherche
print("\nTest de recherche de livres")
livre = rechercher_livre("1984")
if livre:
    print("Livre trouvee")
else:
    print("Livre non trouve")
