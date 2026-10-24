""" Kirjuta programm, mis küsib kasutajalt tema perekonnanime ja sugu (vali "m" või "n").
Programm tervitab kasutajat vastavalt soole:
- Kui kasutaja valib "m", väljasta: "Tere, härra [perekonnanimi]!"
- Kui kasutaja valib "n", väljasta: "Tere, proua [perekonnanimi]!"
- Kui kasutaja sisestab midagi muud, väljasta: "Tere, [perekonnanimi]! (sugu ei olegi tähtis)."
 """

#Alusta programmi
#Küsi kasutajalt "Mis on sinu perekonnanimi?".
#Salvesta vastus muutujasse perekonnanimi.
#Küsi kasutajalt "Sisesta oma sugu (m/n): ".
#Salvesta vastus muutujasse sugu.
#Kui sugu on "m", siis väljasta "Tere, härra " + perekonnanimi + "!"
#Muidu kui sugu on "n", siis väljasta "Tere, proua " + perekonnanimi + "!"
#Muidu väljasta "Tere, " + perekonnanimi + "! (sugu ei olegi tähtis)."
#Lõpeta programm.

perekonnanimi = input("Mis on sinu perekonnanimi? ")
sugu = input("Sisesta oma sugu (m/n): ")

if sugu == "m":
    print("Tere, härra " + perekonnanimi + "!")
elif sugu == "n":
    print("Tere, proua " + perekonnanimi + "!")
else:
    print("Tere, " + perekonnanimi + "! (sugu ei olegi tähtis).")

