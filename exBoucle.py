#ex 1 :

# n = int(input("Entrer votre nombre : "))
# j = 0
# for i in range(1 , n + 1) :
#     j = j + 1/i
# print(j)

#ex 2 :

# n = int(input("Entrer votre nombre : "))
# i = 1
# j = 0
# while i <= n :
#     j = (j + 1) / i
#     i = i + 1
# print(j)

#ex 3 :

# n = int(input("Entrer votre nombre 10^? : "))
# d = 0
# for i in range (0 , n + 1) :
#     d = d + (10 ** i)
# print(d)

#ex 4 :

# n = int(input("Entrer votre nombre : "))
# d = 0
# s = 0
# while s <= n :
#     d = d + 10 ** s
#     s = s + 1
# print(d)

#ex 5 :

# n = int(input("Entrer votre nombre : "))
# j = 1

# while n < 0 :
#     n = int(input("On peut pas faire un calcul factoriel avec un nombre < 0 : "))
# if n == 0 :
#     print("la factoriel de 0 est : 1")
# else :
#     for i in range (1 , n + 1) :
#         j = j * i
#     print("Le calcul factoriel est : ",j)

#ex 6 :

# n = int(input("Entrer votre nombre : "))
# somme = 0
# for i in range (1 , n * 2):
#     if i % 2 == 0 :
#         i = 0
#     somme = somme + i ** 2
# print("La somme des carres des",n,"premiers nombre impair est :",d)

#     une autre solution optimale :

# n = int(input("Entrer votre nombre : "))
# somme = 0
# le_pas = 1
# for i in range (n):
#     somme = somme + (le_pas ** 2)
#     le_pas = le_pas + 2
# print("La somme des carres des",n,"premiers nombre impair est :",somme)

# ex 7 :

# nmbre = 0
# while nmbre < 100 :
#     nmbre+=1
#     print(nmbre)

#ex 8 :

# m = input("Donner votre phrase / mot : ")
# n = 0
# c = ""
# for c in m :
#     if c == "e" or c == "a" or c == "i" or c == "u" or c == "y" or c == "o" :
#         n = n + 1
# print("le nombre de voyelle est :",n)

#ex 9 :

# n = int(input("Donner votre nombre : "))
# for i in range (n , n + 11 , 1) :
#     print(i,end=" ")

#  Demander à l'utilisateur d'entrer un nombre

# nombre_entre = int(input("Entrez un nombre : "))

# i = 1
# while i <= 10:
#     print(nombre_entre + i)
#     i = i + 1

#ex 10 :

# age = int(input("Quel est votre age : "))

# while 0 <= age > 100 :
#     age = int(input("Ce n'est pas un age valide : "))
# if age >= 18 :
#     print("Vous etes majeur")
# else :
#     print("Vous etes mineur")

# ex 11 :

# nombre = int(input("Entrer votre nombre : "))
# while nombre <= 0 :
#     nombre = int(input("Entrer votre nombre il doit pas etre = 0 : "))
# print("les deviseur de",nombre,"sont :")
# for i in range (1 , nombre + 1):
#     if nombre % i == 0 :
#         print(i,end=" ")

# ex 12 :

# age = int(input("Entrer c'est le combien tième anniverssaire : "))
# versement_anuel = 0
# print("La somme est : ")
# for i in range (1 , age + 1):

#     versement_anuel = versement_anuel + (i * 3) + 500
# print(versement_anuel,end=" ")

# ex 13 :

# capital = 1000000
# ville = 500000
# annees = 0
# while capital > ville :
#     ville = ville * 1.08
#     capital = capital + 50000
#     annees = annees + 1
# print("dans",annees,"ans la capital aura :",capital,"habitants et la ville aura :",ville)

# ex 14 :

# n = int(input("Entrer la valeur de n : "))
# u0 = 6 
# for i in range (1 , n + 1):
#     u0 = (4 * u0 + 10)
# print("U",n,"=",u0)

# n = int(input("Entrer la valeur de n > 2 : "))
# while n <= 2 :
#     n = int(input("Entrer la valeur de n elle doit etre superieur a 2 : "))
# u0 = 0
# u1 = 1
# print("la suite de fibonacci est : ")
# print(u0,end=" ")
# print(u1,end=" ")
# for i in range (0 , n - 1):
#     u = u1 + u0
#     print(u,end=" ")
#     u0 = u1
#     u1 = u
    
# n = int(input("Entrer le nombre : "))
# est_premier = True

# if n < 2:
#     est_premier = False
# else:
#     for i in range(2, int(n/2) + 1):
#         if n % i == 0:
#             est_premier = False
#             break

# if est_premier:
#     print(f"Le nombre {n} est un nombre premier.")
# else:
#     print(f"Le nombre {n} n'est pas un nombre premier.")

# n = int(input("Entrer le nombre d'equipe : "))
# for i in range (1 , n + 1):
#     for j in range (1 , n + 1):
#         if i != j :
#             print(i,"vs",j)

import random
n = random.randint(1,30)
num = 5
while num > 0 :
    num -= 1
    valeur = int(input("trouver le nombre qui se trouve entre 1 et 30 : "))
    if valeur < n :
        print("c'est plus !")
    elif valeur > n :
        print("c'est moin !")
    else :
        print(valeur,"est egal a",n,"vous avez trouver")
        break
if num == 0 and valeur != n :
    print("vous avez pas trouver dommage")