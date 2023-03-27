import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_hello_world(self):
        self.assertEqual("Hello world", "Hello world")

class TestMaksukortti(unittest.TestCase):
	def setUp(self):
		self.kortti = Maksukortti(1000)

	def test_konstruktori_asettaa_saldon_oikein(self):
		self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

	def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
		self.kortti.syo_edullisesti()
		self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.50 euroa")

	def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
    		self.kortti.syo_maukkaasti()

    		self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")

	def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
    		kortti = Maksukortti(200)
    		kortti.syo_edullisesti()

    		self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

	def test_kortille_voi_ladata_rahaa(self):
		self.kortti.lataa_rahaa(2500)
		self.assertEqual(str(self.kortti), "Kortilla on rahaa 35.00 euroa")

	def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
		self.kortti.lataa_rahaa(20000)
		self.assertEqual(str(self.kortti), "Kortilla on rahaa 150.00 euroa")

	def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
		kortti = Maksukortti(300)
		kortti.syo_maukkaasti()
		self.assertEqual(str(kortti), "Kortilla on rahaa 3.00 euroa")

	def test_negatiivisen_summan_lataaminen_ei_muuta_kortin_saldoa(self):
		self.kortti.lataa_rahaa(-200)
		self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

	def test_possible_to_buy_cheap_lunch_when_exact_amount_only(self):
		kortti= Maksukortti(250)
		kortti.syo_edullisesti()
		self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")

	def test_can_buy_tasty_lunch_when_exact_amount_only(self):
		kortti=Maksukortti(400)
		kortti.syo_maukkaasti()
		self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")

