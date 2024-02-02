ope = str(input("Entrer l'operation que vous voulez : "))
while ope != "%" and ope != "+" and ope != "-" and ope != "/" and ope != "*" and ope != "**":
    print("Operation non valide !")
    ope = input("Entrer une operation entre / , + , - , % , * , ** : ")
    while ope == "%" or ope == "+" or ope == "-" or ope == "/" or ope == "*" or ope == "**":
        n1 = int(input("Entrer le premier nombre : "))
        n2 = int(input("Entrer le deuxieme nombre : "))
        if ope == "+" :
            print("la somme des 2 est :",n1 + n2)
        elif ope == "/" and n2 != 0 :
            print("la division est :",n1/n2)
        elif ope == "*" :
            print("le resultat de la miltiplication est :",n1*n2)
        elif ope == "-" :
            print("n1 - n2 =",n1 - n2)
        elif ope == "**" :
            print("n1^n2 =",n1 ** n2)
        else :
            print("le reste de n1 / n2 :",n1 % n2)
        quitter_continuer = input("continuer ou arreter : ")
        if quitter_continuer == "continuer" or quitter_continuer == "Continuer":
            ope = str(input("Entrer l'operation que vous voulez : "))
            continue
        else : 
            break