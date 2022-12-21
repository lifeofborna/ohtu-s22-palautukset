
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

def luo_peli(pelimuoto):
        if pelimuoto == "a":
            return KPSPelaajaVsPelaaja()
        elif pelimuoto == "b":
            return KPSTekoaly()
        elif pelimuoto == "c":
            return KPSParempiTekoaly()
        else:
            raise ValueError("Tuntematon pelimuoto")