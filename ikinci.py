#1030530259
#ÖMER MERT DEMİREL
print("Çeviriciye Hoşgeldin!")
veri=input("\nLütfen yazınız: ")                    #takes input from user
print(yazi:="\nverinin uzunluğu", len(veri), "birim")   #with help of WALRUS operator we can calculate lenght in print

secenek=input("\nveriyi neye dönüştürmek istersiniz?(LÜTFEN GEÇERLİ VERİ TİPİ SEÇİN)\n1-integer\n2-string\n3-float\n4-complex\nSeçiniz: ")
secenek=int(secenek) #converts type of input according to user`s choice. 
if secenek==1:       #we need to convert secenek to integer because we cant use comparasion operators
    veri=int(veri)  #type converting
    tip=type(veri)  #type verifying
    print(veri, "veri tipi:", tip)
elif secenek==2:
    print(veri, "zaten bir string tipinde") #since we take it from input func, it is already a string
    tip=type(veri)
elif secenek==3:
    veri=float(veri) #type converting
    tip=type(veri)   #type verifying
    print(veri, "veri tipi:", tip)
elif secenek==4:
    veri=complex(veri) #type converting
    tip=type(veri)     #type verifying
    print(veri, "veri tipi:", tip)
else:
    print("\nyanlış secenek seçtiniz!")
    tip=type(veri)

kimlik=id(veri) # we can learn our variable`s id number in python
yazi=("\nSonuc: {} verisi {} tipinde ve python 'id' numarası: {}")   
print(yazi.format(veri,tip,kimlik)) 