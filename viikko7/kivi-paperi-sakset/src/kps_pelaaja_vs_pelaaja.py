from tuomari import Tuomari
from KPS import KPS

class KPSPelaajaVsPelaaja(KPS):
    def _toisen_siirto(self):
        return input("Toisen pelaajan siirto: ")