#1030520259
#ÖMER MERT DEMİREL
print("var mı? yok mu?`ya Hoşgeldin!!!")
sayi=input("\nlütfen bir sayi ya da kelime gir: ")
#take a string or integer(or many other type) from user
tahmin=input("\nşimdi de içinde var mı yok mu diye bakmak istediğin rakamı veya harfi gir: ")
#take a guess from user
if tahmin in sayi:  #in operator returns true if sayi contains tahmin. 
    print("EVET! içinde var!!!") #if guess is correct in operators returns true
else:
    print("Hayır! malesef içinde yok :( ") #if guess is wrong in operator returns false, so else is active
