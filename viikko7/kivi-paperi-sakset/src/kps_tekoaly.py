from tuomari import Tuomari
from tekoaly import Tekoaly
from KPS import KPS


class KPSTekoaly(KPS):
    def pelaa(self):
        self.tekoaly = Tekoaly()
        super().pelaa()

    def _toisen_siirto(self):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto