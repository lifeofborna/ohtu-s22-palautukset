KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):

        if kapasiteetti is None: self.kapasiteetti = KAPASITEETTI
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None: self.kasvatuskoko = KAPASITEETTI
        else:
            self.kasvatuskoko = kasvatuskoko

        self.taulukko = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.taulukko[i]:
                return True

        return False

    def lisaa(self, alkio):
        if self.alkioiden_lkm == 0:
            self.taulukko[0] = alkio
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True

        if not self.kuuluu(alkio):
            self.taulukko[self.alkioiden_lkm] = alkio
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm % len(self.taulukko) == 0:
                taulukko_old = self.taulukko
                self.taulukko = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.taulukko)

            return True

        return False

    def poista(self, alkio):
        for i in range(0, self.alkioiden_lkm):
            if alkio == self.taulukko[i]:
                self.taulukko[-1] = 0
                for j in range(i, self.alkioiden_lkm-1):
                    apu_taulukko = self.taulukko[j]
                    self.taulukko[j] = self.taulukko[j+1]
                    self.taulukko[j+1] = apu_taulukko
                
                self.alkioiden_lkm = self.alkioiden_lkm - 1
                return True

        return False

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.taulukko[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):

        lukumaarat = {0:"{}", 1:"{" + str(self.taulukko[0]) + "}"}

        if self.alkioiden_lkm in lukumaarat.keys():
            return lukumaarat[self.alkioiden_lkm]
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.taulukko[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.taulukko[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
