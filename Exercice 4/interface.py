def demander_infos():
    # Demande poids et taille
    poids = float(input("Veuillez indiquez votre poids(kg): "))
    taille = float(input("Veuillez indiquez votre taille(): "))
    return(poids,taille)


def afficher_resultat(imc, categorie):
    # Affiche joliment
    print(f"Vous avez un IMC de: {imc:.2f}")
    print(f"Votre categorie est: {categorie}")


import calculs
import interface

poids, taille = interface.demander_infos()
imc = calculs.calculer_imc(poids,taille)
categorie = calculs.interpreter_imc(imc)
interface.afficher_resultat(imc, categorie)
