class Bil:
    def __init__(self,farve):
        self.farve = farve
        self.hjulstr = 17
    
    def udskriv(self):
        print(self.hjulstr, self.farve)


bil = Bil('rød')

bil.udskriv()