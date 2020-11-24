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

for x,y in opslag.items():
    print(x, y)