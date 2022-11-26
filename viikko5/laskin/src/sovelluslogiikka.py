class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.tulokset = []
        self.tulokset.append(tulos)
    
    def miinus(self, arvo):
        self.tulos = self.tulos - arvo
        self.tulokset.append(self.tulos)

    def plus(self, arvo):
        self.tulos = self.tulos + arvo
        self.tulokset.append(self.tulos)

    def nollaa(self):
        self.tulos = 0
        self.tulokset.append(self.tulos)

    def aseta_arvo(self, arvo):
        self.tulos = arvo
        self.tulokset.append(self.tulos)
    
    def kumoa(self):
        if len(self.tulokset) != 0:
            self.tulokset.pop()
            try:
                self.tulos = self.tulokset[-1]
            except:
                self.tulos = 0
        else:
            self.tulos = 0
        