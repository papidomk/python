# nombre = int(input("Entrer votre nombre : "))
# v = ""
# for i in range (nombre) :
#     v = v + "*"
#     print(v)

# autre façon :

nombre = int(input("Entrer votre nombre : "))
for i in range (1 , nombre + 1) :
    for j in range (i) :
        print("* ",end="")
    print("")