from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from KPS import KPS


class KPSParempiTekoaly(KPS):
    def pelaa(self):
        self.tekoaly = TekoalyParannettu(10)
        super().pelaa()

    def _pelaa_kierros(self, ekan_siirto, tuomari):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self.tekoaly.aseta_siirto(ekan_siirto)
        return tokan_siirto