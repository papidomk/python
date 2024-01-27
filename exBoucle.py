# n = int(input("Entrer votre nombre : "))
# j = 0
# for i in range(1 , n + 1) :
#     j = j + 1/i
# print(j)

# n = int(input("Entrer votre nombre : "))
# i = 1
# j = 0
# while i <= n :
#     j = (j + 1) / i
#     i = i + 1
# print(j)

# n = int(input("Entrer votre nombre 10^? : "))
# d = 0
# for i in range (0 , n + 1) :
#     d = d + (10 ** i)
# print(d)

# n = int(input("Entrer votre nombre : "))
# d = 0
# s = 0
# while s <= n :
#     d = d + 10 ** s
#     s = s + 1
# print(d)

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

# n = int(input("Entrer votre nombre : "))
# somme = 0
# for i in range (1 , n * 2):
#     if i % 2 == 0 :
#         i = 0
#     somme = somme + i ** 2
# print("La somme des carres des",n,"premiers nombre impair est :",d)

# une autre solution optimale :

n = int(input("Entrer votre nombre : "))
somme = 0
le_pas = 1
for i in range (n):
    somme = somme + (le_pas ** 2)
    le_pas = le_pas + 2
print("La somme des carres des",n,"premiers nombre impair est :",somme)