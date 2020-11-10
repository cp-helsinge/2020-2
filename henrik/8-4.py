opslag = {
    'dyr': "giraf",
    'bil': "skoda",
    'femten':"atten",
}
print(opslag)

opslag[27] ="Otteogtyve"
opslag[48] ="Tres"
opslag["femten"] ="15"
print(opslag)

for x in opslag.values():
    print(x)