n = int(input("Donner le chiffre entre 2 / 4 / 6 / 8 : "))
if n == 2 :
    print("le joueur va en bas")
elif n == 4 :
    print("le joueur va à gauche")
elif n == 6 :
    print("le joueur va à droite")
elif n == 8 :
    print("le joueur va en haut")
else :
    print("Erreur de saisie le joueur ne bouge pas")