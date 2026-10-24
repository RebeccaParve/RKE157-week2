""" Arstid soovitavad juua päevas 2 liitrit vett.
Kirjuta programm, mis küsib kasutajalt, kui palju klaase vett ta juba joonud on. Oletame, et üks klaas = 250 ml.
Programm arvutab, mitu protsenti päevanormist on täidetud, ja annab tagasisidet:
Kui protsent < 50: väljasta: „Joo rohkem vett, keha vajab seda!“
Kui protsent < 100: väljasta: „Tubli, jätka samas vaimus!“
Kui protsent ≥ 100: väljasta: „Suurepärane, oled oma päevase eesmärgi täitnud!“ """

#Alusta programmi
#Küsi kasutajalt "Mitu klaasi vett oled täna joonud?".
#Salvesta vastus muutujasse klaasid.
#Arvuta joogikogus: klaasid * 250.
#Salvesta päevanorm muutujasse päevanorm = 2000.
#Arvuta protsent: (joogikogus / päevanorm) * 100.
#Salvesta tulemus muutujasse protsent.
#Kui protsent < 50, siis väljasta: "Joo rohkem vett, keha vajab seda!"
#Muidu kui protsent < 100, siis väljasta: "Tubli, jätka samas vaimus!"
#Muidu (kui protsent ≥ 100), siis väljasta: "Suurepärane, oled oma päevase eesmärgi täitnud!"
#Lõpeta programm.

klaasid = int(input("Mitu klaasi vett oled täna joonud?:"))
joogikogus = klaasid * 250
päevanorm = 2000
protsent = (joogikogus / päevanorm) * 100

print("Päevanormist on täidetud", protsent, "%.")

if protsent < 50:
    print("Joo rohkem vett, keha vajab seda!")
elif protsent < 100:
    print("Tubli, jätka samas vaimus!")
else:
    print("Suurepärane, oled oma päevase eesmärgi täitnud!")

