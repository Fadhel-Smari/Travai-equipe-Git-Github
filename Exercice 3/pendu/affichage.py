# #Intro au jeux / duplicat..
# def affichage_depart():
#     print("=== Jeu du Pendu ===")

#affiche different stage de pendu
def afficher_pendu(erreurs):
    stage = [
        '''
  ¤---¬
  |   |
      |
      |
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
 /|   |
      |
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
 /|\\  |
 /    |
      |
=========
        ''',
        '''
  ¤---¬
  |   |
  Ø   |
 /|\\  |
 / \\  |
      |
=========
        ''',]
    print(stage[erreurs])
