import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_initial_balance_correct(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_loading_money_functions_correctly(self):
        self.maksukortti.lataa_rahaa(3000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 40.00 euroa")

    def test_withdrawing_money_if_enough_balance(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")
    
    def test_withdrawing_if_not_enough_balance(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_withdrawing_if_not_enough_balance_returns_False(self):
        self.assertEqual(bool(self.maksukortti.ota_rahaa(2000)), False)
    
    def test_withdrawing_if_enough_balance_returns_True(self):
        self.assertEqual(bool(self.maksukortti.ota_rahaa(500)), True)

        