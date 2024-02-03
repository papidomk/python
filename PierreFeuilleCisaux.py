import random
personne = input("Choisissez Pierre Feuille ou Cisaux : ")
pierre = "Pierre"
cisaux = "cisaux"
feuille = "Feuille"
score = 0
score_ordi = 0
while personne != pierre and personne != feuille and personne != cisaux :
    personne = input("La reponse doit etre Pierre , Feuille ou Cisaux : ")
ordi = random.randint(1 , 3)
while personne == pierre or personne == cisaux or personne == feuille :
    if ordi == 1 :
        ordi = pierre 
        if personne == ordi :
            print(personne,"VS",ordi,"match nul")
        elif personne == cisaux :
            print(personne,"VS",ordi,"J'ai gagner")
            score_ordi += 1
        else :
            print(personne,"VS",ordi,"Vous avez gagner")
            score += 1
    elif ordi == 2 :
        ordi = cisaux
        if personne == ordi :
            print(personne,"VS",ordi,"match nul")
        elif personne == feuille :
            print(personne,"VS",ordi,"J'ai gagner")
            score_ordi += 1
        else :
            print(personne,"VS",ordi,"Vous avez gagner")
            score += 1
    elif ordi == 3 : 
        ordi = feuille
        if personne == ordi :
            print(personne,"VS",ordi,"match nul")
        elif personne == pierre :
            print(personne,"VS",ordi,"J'ai gagner")
            score_ordi += 1
        else :
            print(personne,"VS",ordi,"Vous avez gagner")
            score += 1
    print("Le score est de :",score,"TOI ,",score_ordi,"MOI")
    
    continuer_arreter = input("Continuer ou Arreter : ")
    if continuer_arreter != "continuer" :
        break