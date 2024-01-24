#ex 1 :
"""
nmbre_A = input("donner le premier nombre : ")
nmbre_B = input("donner le deuxieme nombre : ")
print("la somme des nombre est : ",int(nmbre_A)+int(nmbre_B))
"""
#ex 2 :
"""
nombre = int(input("donner un nombre : "))
if (nombre%2) == 0 :
   print("ton nombre est pair")
else :
   print("votre nombre est impair")
"""
#ex 3 :
"""
nmbre = 0
while nmbre < 100 :
    nmbre+=1
    print(nmbre)
"""
#ex 4 :
"""
age = int(input("Quel est votre age : "))

while 0 <= age > 100 :
    age = int(input("Ce n'est pas un age valide : "))
if age >= 18 :
    print("Vous etes majeur")
else :
    print("Vous etes mineur")
"""
#ex 5 :
"""
age = int(input("Quel est votre age : "))
prenom = input("Quel est votre prenom : ")
print("Bienvenue a l'universite",prenom,"tu as",age,"ans")
"""
#ex 6 : 
"""
a = float(input("donner votre premiere note : "))
b = float(input("donner votre deuxieme note : "))
c = float(input("donner votre troisieme note : "))
d = float(input("donner votre quatrieme note : "))
e = float(input("donner votre cinqieme note : "))
somme = a + b + c + d + e
moyenne = somme/5
print("la somme des note est :",somme,"et la moyenne est de :",moyenne)
"""
#ex 7 :
"""
import math
r = float(input("Donner le rayon de la sphere : "))
v = (4*r**3*math.pi)/3
print("Le rayon de la sphere est de : ",v)
"""
#ex 8 :
"""
a = int(input("Donner le nombre a : "))
b = int(input("Donner le nombre b : "))
c = a
a = b
b = c

print(a,"et",b)
"""
#ex 9 :
"""
def conversion_temp():
    temp = int(input("donner le temp en s : "))
    temp_h = int(temp // 3600)
    temp_hm = temp % 3600
    temp_min = int(temp_hm // 60)
    temp_s = int(temp_hm % 60)
    print("le temp est : ",temp_h,"h",temp_min,"min",temp_s,"s")

conversion_temp()
"""
#ex 10 :
"""
def distance_point():
    xa = int(input("Donner Xa : "))
    ya = int(input("Ya : "))
    xb = int(input("Xb : "))
    yb = int(input("Yb : "))
    xab = xb - xa
    yab = yb - ya
    print("la distance est : ",xab,";",yab)
distance_point()
"""
#ex 11 : 
"""
a = int(input("Donner le nombre A : "))
b = int(input("Donner le nombre B : "))
if (a < 0 and b > 0) or (b < 0 and a > 0) :
    print(a, "et" ,b,"sont pas du meme signe")
else :
    print(a, "et" ,b,"sont du meme signe")
"""
#ex 12 :
"""
a = float(input("Donner le nombre A : "))
b = float(input("Donner le nombre B : "))
if a*b > 0 :
    c = a
    a = b
    b = c
    print("Changements des sommes A : ",a, " B : ",b)
else :
    s = a + b
    d = a * b
    a = s
    b = d
    print("la somme des deux est : ",a, "le proDuit des deux est : ",b)
"""
#ex 13 :
"""
p = int(input("Combien de photocopie voulez vous faire : "))
if (p <= 10) :
    prix = p * 0.30
elif (p > 10) and (p <= 30) :
    prix = 10 * 0.3 + (p - 10) * 0.25
else :
    prix = 10 * 0.3 + 20 * 0.25 +(p - 30) * 0.20
print("le prix est : ",prix,"euro")
"""
#ex 14 :
age = int(input("Quel est votre age : "))
while age < 6 :
    age = int(input("vous devez avoir plus de 6 ans : "))
if age == 6 or age == 7  :
    cate = "poussain"
elif age == 8 or age == 9 :
    cate = "pupille"
elif age == 10 or age == 11 :
    cate = "minime"
elif age > 12 :
    cate = "cadet"

print("votre categorie :",cate)

#ex 15 :

