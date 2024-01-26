c = input("Entre votre charactere : ")
if ("a"<= c <= "z") or ("A"<= c <= "Z") :
    print("votre character est une lettre")
elif "0"<= c <="9" :
    print("votre charactere est un nombre")
else :
    print("votre charactere est un charectere special")