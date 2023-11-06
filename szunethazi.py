## 1.feladat

def intervallum():

    szam1 = int(input("Adj meg egy [200, 920] intervallumban lévő egész számot: "))

    if 200 <= szam1 <= 920:
        elso = int(str(szam1)[0])
        print("Az első számjegy:", elso)
    else:
        print("Hiba: A megadott szám nincs az [200, 920] intervallumban.")



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


