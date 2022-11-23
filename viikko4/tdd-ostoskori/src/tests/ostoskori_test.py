import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.auto = Tuote("auto",1)
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(),0)


    def test_yksi_tuote_yksi_tavara(self):
        self.kori.lisaa_tuote(self.auto)

        self.assertEqual(self.kori.tavaroita_korissa(),1)
    
    def test_ostoskorin_hinta_sama_kuin_tuotteen(self):
        self.kori.lisaa_tuote(self.auto)

        self.assertEqual(self.auto.hinta(), self.kori.hinta())
    
    def test_ostoskorin_määrä_on_kaksi_eri_tuote(self):
        self.kori.lisaa_tuote(self.auto)
        self.kori.lisaa_tuote(Tuote("es",1))

        self.assertEqual(self.kori.tavaroita_korissa(),2)
    
    def test_ostoskorin_määrä_on_kaksi_ja_hinta_on_summa(self):
        self.kori.lisaa_tuote(self.auto)
        self.kori.lisaa_tuote(Tuote("es",1))

        self.assertEqual(self.kori.hinta(),2)
    
    def test_kahden_saman_tuotteen_lisäys_2_tavaraa(self):
        self.kori.lisaa_tuote(self.auto)
        self.kori.lisaa_tuote(self.auto)

        self.assertEqual(self.kori.tavaroita_korissa(),2)
    
    def test_kahden_saman_lisäys_on_2x_hinta(self):
        self.kori.lisaa_tuote(self.auto)
        self.kori.lisaa_tuote(self.auto)

        self.assertEqual(self.kori.hinta(),self.auto.hinta()*2)