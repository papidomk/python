n1 = int(input("Entrer votre nombre a : "))
n2 = int(input("Entrer votre nombre b : "))
while n2 != 0 :
    temp = n2
    n2 = n1 % n2
    n1 = temp
print("Le PGCD est :",n1)