from math import *
#1
print("Tere maailm!")
nimi=input("Mis on sinu nimi? ").capitalize()
print(f"Tere maailm1, Tervitan sind {nimi}")
vanus=int(input("Kui vana sa oled?"))
print(f"Tere maailm1, Tervitan sind {nimi} ! Sa oled {vanus} aastat vana.")

#2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print(f"Muutuja {vanus} on {type(vanus)}")
print(f"Muutuja {eesnimi} on {type(eesnimi)}")
print(f"Muutuja {pikkus} on {type(pikkus)}")
print(f"Muutuja {kas_käib_koolis} on {type(kas_käib_koolis)}")

#3
from random import *
kommide_arv=randint(10,100)
print(f"laua peal on {kommide_arv}")
mitu=int(input("Mitu tahad süüja?"))
print(f"Laua peal on jäänud {kommide_arv-mitu}")

#4
Pikkus = int(input("Mis on puu pikkus: *"))
print(f"Puu labimoot on {Pikkus / pi} ")

#5 harjutus
N = float(input("Sisesta ristkuliku pikkus (m): "))
M = float(input("Sisesta ristkuliku laius (m): "))

diagonaal = sqrt(N**2 + M**2)

print(f"Ristkuliku diagonaali pikkus on {diagonaal} meetrit.")

#6
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg                                      #ошибка, действия наоборот

print("Teie keskmine kiirus on:", kiirus, "km/h")

#7
arv1 = int(input("Esimene: "))
arv2 = int(input("Teine: "))
arv3 = int(input("Kolmas: "))
arv4 = int(input("Neljas: "))
arv5 = int(input("Viies: "))
keskmine = (arv1 + arv2 + arv3 + arv4 + arv5) / 5

print("Sisestatud arvude aritmeetiline keskmine on:", keskmine)

#8
print("  @..@")
# print(" (----)")
# print("( \\__/ )")
# print(" ^^ "" ^^")

#9
# Küsime kasutajalt kolmnurga külgede pikkused
a = int(input("Sisesta esimese külje pikkus: "))
b = int(input("Sisesta teise külje pikkus: "))
c = int(input("Sisesta kolmanda külje pikkus: "))
P = a + b + c

# print("Kolmnurga ümbermõõt on:", P)

# #10

pitsa_hind = 12.90
jootraha_protsent = 0.10
jootraha = pitsa_hind * jootraha_protsent
kogusumma = pitsa_hind + jootraha
maksab_iga_üks = kogusumma / 2

print(f"Igaüks peab maksma: {maksab_iga_üks}€")







