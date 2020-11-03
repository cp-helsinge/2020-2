import random

byer=["Hillerød","Aarhus","Sønderborg","Åbenrå","Farum","Esrum","Gundsømagle"]
print(byer)
byer[1] = "Græsted"
print(byer)

for punkt in byer:
    print(punkt)

print(random(punkt))

if "Græsted" in byer:
    print("Græsted er en dejlig by")
