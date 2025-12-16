vie_restant = 0
#Intro au jeux
def affichage_depart():
    print("=== Jeu du Pendu ===")

#affiche different stage de pendu, nb vie et game over
def afficher_pendu(erreurs):
    print(f"{vie_restant}/6 vie")
    stage = [
        '''
  ¤---¬
  |   |
  Ø   |
 /|\\  |
 / \\  |
      |
=========
        ''',
        '''
  ¤---¬
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
        ''',
        '''
  ¤---¬
  |   |
  O   |
 /|\\  |
      |
      |
=========
        ''',
        '''
  ¤---¬
  |   |
  O   |
 /|   |
      |
      |
=========
        ''',
        '''
  ¤---¬
  |   |
  O   |
  |   |
      |
      |
=========
        ''',
        '''
  ¤---¬
  |   |
  O   |
      |
      |
      |
=========
        ''',
        '''
  ¤---¬
  |   |
      |
      |
      |
      |
=========
        ''',]
    print(stage[erreurs])
    if vie_restant == 0:
        print("=== Vous avez perdu ===")


#affiche le nom du jeux
affichage_depart()
#affiche la progression du jeux
afficher_pendu(vie_restant)
