# n = int(input("Donner votre nombre : "))
# for i in range (n , n + 11 , 1) :
#     print(i,end=" ")

# Demander à l'utilisateur d'entrer un nombre
nombre_entre = int(input("Entrez un nombre : "))

i = 1
while i <= 10:
    print(nombre_entre + i)
    i = i + 1
