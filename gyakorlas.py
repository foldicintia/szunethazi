
import random
import math

"""Véletlen számok generálása"""

def veletlen():
# [10,30]
    i:int = 0
    while i<10:
        szam:int = math.floor (random.random()*21 + 10)
        print(szam, end=" ")
        i+=1

"""
1. generálj 5 véletlen lottószámot [1,90]
"""
def elso():
    i:int = 0
    while i<5:
        szam:int = math.floor (random.random()*81 + 10)
        print(szam, end=" ")
        i+=1

"""
2. generálj 1 véletlen kétjegyű számot, döntsd el róla hogy páros vagy páratlan
"""
def masodik():
    i:int = 0
    szam:int = math.floor(random.random()*90+10)
    if szam%2 ==0:
        print(f"{szam} páros")
    else:
        print(f"{szam} páratlan")
    i+=1


"""
3. generálj 15 db egész számot [0,1] között
Hány 1-est generáltál?
"""
def harmadik():
    i:int = 0
    while i<15:
        szam:int = math.floor (random.random()*2)
        print(szam, end=" ")
        i+=1
"""
4. generálj egy véletlen számot 1 és 10 között 
szorozd meg 3-mal
vonj ki belőle 15-öt
oszd el 6-tal 
szorozd be 2-vel
vond ki belőle az eredeti számot
A program írja ki, hogy az eredmény egyenlő-e 5-tel
[1,10]
"""
def negyedik():
    i:int = 0
    szam:int = math.floor(random.random()*9+1)
    
    szorzas = szam * 3
    print(szorzas, end=", ")
    
    kivonas = szorzas - 15
    print(kivonas, end=", ")
    
    osztas = kivonas / 6
    print(osztas, end=", ")
    
    szorzas2 = osztas * 2
    print(szorzas2, end=", ")
    
    kivonas2 = szorzas2 - szam
    print(kivonas2, end=", ")

    if kivonas2 == 5:
        print(f"{kivonas2} egyenlő 5-tel")
    else:
        print(f"{kivonas2} nem egyenlő 5-tel")
    i+=1


"""5. írj metódust"""