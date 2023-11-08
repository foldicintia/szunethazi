## 1.feladat

def intervallum():
    szam1 = int(input("Adj meg egy számot [200, 920] intervallumban: "))
    while not (200 <= szam1 <= 920):
        szam1 = int(input("Adj meg egy számot [200, 920] intervallumban: "))

    elso = int(str(szam1)[0])
    print("Az első számjegy:", elso)


## 4.feladat

def ertekeles(szam4):

    szam4 = int(input("Adj meg egy óra számot 1 és 9 között: ")) 

    if szam4 == 1:
        print("Még 90% on vagyunk!")
    elif szam4 in (2, 3):
        print("Még bírjuk (60%).")
    elif szam4 in (4, 5, 6, 7):
        print("Progit tanulunk, töltődünk! 70%")
    elif szam4 in (8, 9):
        print("Lassan nem bírjuk tovább! 50%")
    elif szam4 > 9:
        print("Ez már tényleg túlzás.")
    else:
        print("Be se jövök!")


## 6.feladat

import math

def negyzetgyok_szamitas():
    szam = float(input("Adj meg egy valós számot: "))
    
    if szam < 0:
        print("Hiba: Negatív számból nem lehet négyzetgyököt vonni!")
    else:
        gyok = math.sqrt(szam)
        print(f"A(z) {szam} négyzetgyöke: {gyok}")


def szam_szamjegye(szam:int):
    print("szám: ", szam)
    while(szam>9):
        print("következő számjegy", szam%10)
        szam= szam//10
        print("az aktuális szám ", szam)
    print("az utolsó számjegy ", szam)

def szam_szamjegye2(szam:int):
    szoveg_szam: str(szam)
    i=0
    while i<len(szoveg_szam):
        print(szoveg_szam[i])
        i+=1

def erme_dobas():
    i:int = 0 
    f_szam:int = 0
    f_hossz = 0
    elozo_string_f=False 
    max_hossz = 0
    while i<10:
        jel:str = input("F/I: ")
        while not(jel == "F" or jel == "f" or jel == "I" or jel == "i"):
            jel:str = input("nem jó, F/I -t adj meg!:")
        if (jel == "F" or jel == "f"):
            f_szam+=1
            if elozo_string_f:
                f_hossz+=1
            elozo_string_f=True
        else:
            print("aktuális hossz: ", f_hossz)
            elozo_string_f=False
            """Itt ossze fogjuk hasonlitani az eddigi max_hosszt az aktualis hosszal"""
            if (max_hossz<f_hossz):
                max_hossz=f_hossz
            f_hossz = 0

        i+=1
    print("aktuális hossz: ", f_hossz)
    if (max_hossz<f_hossz):
        max_hossz=f_hossz
    print("F-ek száma: ", f_szam)
    print("maximális F hossz:", max_hossz)

