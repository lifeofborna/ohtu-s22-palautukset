from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoskori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return len(self.ostoskori)
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        if len(self.ostoskori) >= 1:
            summa = 0
            for i in self.ostoskori:
                summa+=i.hinta()
            return summa
        else:
            return 0
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        self.ostoskori.append(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        self.ostoskori.remove(poistettava)

    def tyhjenna(self):
        for x in self.ostoskori:
            self.ostoskori.remove(x)
        # tyhjentää ostoskorin

    def ostokset(self):
        ostokset_l = []
        nimet = []
        for x in self.ostoskori:
            if x.nimi() in nimet:
                for y in ostokset_l:
                    if y.tuotteen_nimi() == x.nimi():
                        y.muuta_lukumaaraa(1)
            else:   
                ostokset_l.append(Ostos(x))
                nimet.append(x.nimi())

        return ostokset_l
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on