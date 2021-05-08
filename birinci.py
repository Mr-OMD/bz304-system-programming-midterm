#1030520259
#ÖMER MERT DEMİREL
import sys                      #to use in future we added sys library
matematikKredi=4
FizikKredi=3                    #we have 3 courses which has predefined credits
AlgoritmaKredi=6
print("GanoMatik`e hoşgeldiniz\n") #welcome string and new line witn \n
MatNot=input("Lütfen Matematik dersi notunuzu giriniz: ") #take course grade from user and save it to MatNot
MatNot=int(MatNot)                  #to use Grade in calculations we need to convert its type to int from string
if MatNot<=30:                      #because input function takes as string
    matHarf="FF"
    matagr=0.0
elif MatNot<=40:
    matHarf="FD"
    matagr=0.5
elif MatNot<=50:                    #With conditional statement block it determines letter grade
    matHarf="DD"                    #and weighted grade of that letter grade
    matagr=1.0
elif MatNot<=60:
    matHarf="DC"
    matagr=1.5
elif MatNot<=70:
    matHarf="CC"
    matagr=2.0
elif MatNot<=80:
    matHarf="CB"
    matagr=2.5
elif MatNot<=85:
    matHarf="BB"
    matagr=3.0
elif MatNot<=90:
    matHarf="BA"
    matagr=3.5
else:
    matHarf="AA" 
    matagr=4.0  

FizNot=input("Lütfen Fizik dersi notunuzu giriniz: ")
FizNot=int(FizNot)                      #it does same things for Fizik course as Matematik course
if FizNot<=30:
    fizHarf="FF"
    fizagr=0.0
elif FizNot<=40:
    fizHarf="FD"
    fizagr=0.5
elif FizNot<=50:
    fizHarf="DD"
    fizagr=1.0
elif FizNot<=60:
    fizHarf="DC"
    fizagr=1.5
elif FizNot<=70:
    fizHarf="CC"
    fizagr=2.0
elif FizNot<=80:
    fizHarf="CB"
    fizagr=2.5
elif FizNot<=85:
    fizHarf="BB"
    fizagr=3.0
elif FizNot<=90:
    fizHarf="BA"
    fizagr=3.5
else:
    fizHarf="AA"
    fizagr=4.0 

AlgNot=input("Lütfen Algoritma dersi notunuzu giriniz: ")
AlgNot=int(AlgNot)                          ##it does same things for Algoritma course as Matematik course
if AlgNot<=30:
    algHarf="FF"
    algagr=0.0
elif AlgNot<=40:
    algHarf="FD"
    algagr=0.5
elif AlgNot<=50:
    algHarf="DD"
    algagr=1.0
elif AlgNot<=60:
    algHarf="DC"
    algagr=1.5
elif AlgNot<=70:
    algHarf="CC"
    algagr=2.0
elif AlgNot<=80:
    algHarf="CB"
    algagr=2.5
elif AlgNot<=85:
    algHarf="BB"
    algagr=3.0
elif AlgNot<=90:
    algHarf="BA"
    algagr=3.5
else:
    algHarf="AA"
    algagr=4.0 

#it prints letter grades for each course with help of format function.Also \t for new tab and \n for new line
#is used for better understanding
yazi="Matematik harf notunuz:\t {} \nFizik harf notunuz:\t {} \nAlgoritma harf notunuz:\t {} \n"
print(yazi.format(matHarf,fizHarf,algHarf))

#it calculates ToplamKredi from predefined course credits
ToplamKredi=matematikKredi+FizikKredi+AlgoritmaKredi

#with help of the eval() function it calculates weighted grades and calculates cumulative grade point avarage
Agirlikli=eval("matematikKredi*matagr+FizikKredi*fizagr+AlgoritmaKredi*algagr")
Gano=Agirlikli/ToplamKredi
print("GANO: ", round(Gano,2))          #prints GANO. round function makes float number round 2 digits after zero

#this part is creating report file in txt format with write permission
f=open("rapor.txt","w")
print(yazi.format(matHarf,fizHarf,algHarf),file=f) #it writes previosly created string into that report file
oldout=sys.stdout                     #this part is to show diffrent way to do it     
sys.stdout=f                          #we imported sys at the beginning so we can change the output direction
print("\nGANO: ", round(Gano,2))      #it changed output direction from console to that file and write GANO 
sys.stdout=oldout                     #then changed back to standart output direction
f.close()                             #finally closed our file
