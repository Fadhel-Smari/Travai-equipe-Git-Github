# Orchestre tout + tests unitaires

from calculs import calculer_imc, interpreter_imc
from interface import demander_infos, afficher_resultat
from historique import sauvegarder_calcul, afficher_historique

def main():
    nom, poids, taille = demander_infos()
    imc = calculer_imc(poids, taille)

    categorie = interpreter_imc(imc)
    afficher_resultat(nom, imc, categorie)

    sauvegarder_calcul(nom, imc)

if __name__ == "__main__":
    main()