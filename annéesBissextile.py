annes = int(input("Donner l'année : "))
if (annes % 4 == 0 ) and (annes % 100 != 0) :
    print("votre annees est bissextille")
else :
    print("votre annees est pas bissextille")