import math
import time

#Zmienne
sumao = 0
waga = 0
licznik = 0

#Sczytywanie danych
inp_o = input("Podaj oceny(po przecinku i spacji): ")
inp_w = input("Podaj wagi ocen(po przecinku i spacji): ")

print(inp_o.count(","))
powtu = inp_o.count(",")
while licznik != powtu:
   #Liczenie
    aktoc = int(inp_o[:inp_o.index(",")])
    aktwag  = int(inp_w[:inp_w.index(",")])
    sumao = sumao + (aktoc * aktwag)
    waga = waga + aktwag
    inp_o = inp_o[inp_o.index(",") + 2:]
    inp_w = inp_w[inp_w.index(",") + 2:]
    licznik = licznik + 1

#Podsumowywanie
waga = waga + int(inp_w)     
sumao = sumao + (int(inp_o) * int(inp_w))
srednia = int(sumao) / int(waga)


ocena = 0
srednia_st = str(srednia)

#Zaokrąglanie
if (srednia - math.floor(srednia)) * 100 >= 60:
    ocena = srednia + 1
else:
    ocena = math.floor(srednia)

#info
print("Twoja średnia to {b}".format(b=srednia))
print("")
print("Wychodzi ocena: {e}".format(e=ocena))
print("")
print("Suma twoich ocen: {a}".format(a=sumao))
print("")
print("Łączna waga twoich ocen: {c}".format(c=waga))
time.sleep(20)