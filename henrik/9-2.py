class Bil:
    def __init__(self,farve):
        self.farve = farve
        self.hjulstr = 17
bil = Bil('rød')
print(bil.hjulstr)
print(bil.farve)