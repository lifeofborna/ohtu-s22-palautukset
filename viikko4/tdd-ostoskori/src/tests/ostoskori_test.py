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
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        # testaa että metodin palauttaman listan pituus 1
        self.assertEqual(len(ostokset), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(),"Maito" )
        self.assertEqual(self.kori.tavaroita_korissa(),1 )
    
    def test_eri_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(self.auto)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset),2 )
    
    def test_kahden_saman_tuotteen_lisäys_ostos_samanimi_ja_lkm_2(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(ostokset[0].tuotteen_nimi(),"Maito")
        self.assertEqual(ostokset[0].lukumaara(),2)
    
    def test_jos_2_samaa_ja_yksi_poistetaan_jää_1kpl(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.kori.poista_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(ostokset[0].lukumaara(),1)