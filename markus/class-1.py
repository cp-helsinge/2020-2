class Ost:
    def __init__(self, farve):
        self.farve = farve
        self.hulstørelse = 5
        self.larve = True
    def udskriv(self):
        print("|", self.hulstørelse,"|", self.farve, "|", self.larve, "|")

ost = Ost("negativ gul")


