# Fonction pour calculer IMC (IMC = poids / taille²)
def calculer_imc(poids, taille):
    imc = poids / (taille ** 2)
    return imc

# Fonction pour iterprèter l'IMC selon les catégories
# Catégories basées sur les classifications de Santé Canada
def interpreter_imc(imc):
    if imc < 18.5:
        return "Poids insuffisant"
    elif 18.5 <= imc < 25.0:
        return "Poids normal"
    elif 25.0 <= imc < 30.0:
        return "Excès de poids"
    elif 30.0 <= imc < 35.0:
        return "Obésité, classe I"
    elif 35.0 <= imc < 40.0:
        return "Obésité, classe II"
    else:
        return "Obésité, classe III"