#1

"""
1. Feladat
Írj egy programot, amely 5 darab véletlenszámot generál [1;7] intervallumon, és ezeket eltárolja egy listában. Kérjen be a felhasználótól egy számot, és vizsgálja meg, hogy ez előfordul-e a listában! Az eredményről tájékoztassa a felhasználót, és írja ki a lista elemeit a képernyőre!
"""
"""
import random
lista = []
for i in range(5):
    lista.append(random.randint(1, 7))
szam = int(input("Kérek egy számot: "))
print(lista)

if szam in lista:
    print(f"A {szam}-es szám van a listában")
    
else:
    print(f"A {szam}-es szám nem találhato a listában")
"""    

#-----------------------------------------------

#2.1
"""
2.1 Feladat
A program tároljon el egy szót egy változóban, majd írja ki egymás alá a szóban található betűket.
"""
"""
szo = "alma"
print(szo)
for i in szo:
    print(i)
"""

#---------------------------------------

#2.2

"""
2.2 Feladat
A program tároljon el egy szót egy változóban. A felhasználó adjon meg egy betűt, amiről a program döntse el, hogy előfordul-e a szóban! Az eredményről tájékoztassa a felhasználót, és írja ki a tárolt szót is!

"""
"""
szo = "alma"
betu = input("Kérek egy betüt: ")
print(szo)
if betu in szo:
    print(f"A {betu}-betű benne van a szóban")
else:
    print(f"A {betu}-betű nincs benne van a szóban")
"""

#-----------------------------------------------------

#2.3
"""
2.3 Feladat
Fejlesszük tovább a 2.2 programot úgy, hogy a felhasználónak többször is legyen lehetősége újabb tippet megadnia. A bekérés addig folytatódjon, amíg a felhasználó nem ad meg betűt, csupán egy ENTER-t üt
"""
"""
szo = "alma"
while True:
    betu = input("Kérek egy betüt: ")
    if betu == "":
        break
    if betu in szo:
        print(f"A {betu}-betű benne van a szóban")
    else:
        print(f"A {betu}-betű nincs benne van a szóban")
print(szo)
"""
#------------------------------------

#2.4

"""
2.4 Feladat
Fejlesszük tovább a 2.3 programot úgy, hogy a program egy listában tároljon öt darab szót, és abból véletlenszerűen válasszon egyet, aminek kapcsán a felhasználó megpróbálja kitalálni a betűit.
"""

"""

from random import choice

lista = ["alma", "körte", "banan", "repa", "barack"]
print(lista)
random_szo = choice(lista)
while True:
    betu = input("Kérek egy betüt: ")
    if betu == "":
        break
    if betu in random_szo:
        print(f"A {betu}-betű benne van a szóban")
    else:
        print(f"A {betu}-betű nincs benne van a szóban")
print(random_szo)
"""

#-----------------------------------------------------------------

#3.1

"""
3.1 Feladat
Torpedó játék egyszerűsített változata. A játéktér legyen egy 3x3-as négyzetalakú rács, amiben az oszlopokat betűk (A, B, C), a sorokat számok (1, 2, 3) jelölik. A program helyezzen el egy darab egy egység kiterjedésű hajót a játéktérben véletlenszerűen (Pl: B2). A játékos próbálja meg kitalálni a hajó pozícióját újabb és újabb tippek megadásával. A játék végén a program azt is írja ki a képernyőre, hogy hány próbálkozásból tudta a játékos kitalálni a pozíciót!
"""

sor = 1
while sor <= 3:
    oszlop = 1
    while oszlop <= 3:
        print('O ', end='')
        oszlop = oszlop + 1
    print('')
    sor = sor + 1     


