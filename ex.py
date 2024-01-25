age = int(input("Donner votre age : "))
sexe = input("donner votre sexe : ")
if sexe == "homme" and age >= 20 :
    print("vous payer les impots")
elif sexe == "femme" and 18 == age <= 35 :
    print("vous payer les impots")
else :
    print("vous payer pas les impots")