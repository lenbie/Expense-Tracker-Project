import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate=Kassapaate()

    def test_initial_cashterminal_money_correct(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_initial_cashterminal_no_cheap_lunches_sold(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_initial_cashterminal_no_expensive_lunches_sold(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_payment_cheap_lunch_sufficient_money_increases(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_payment_cheap_lunch_sufficient_correct_change(self):
        r=self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(r, 60)
    
    def test_payment_cheap_lunch_sufficient_lunches_sold_increases(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_payment_expensive_lunch_sufficient_money_increases(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_payment_expensive_lunch_sufficient_correct_change(self):
        r=self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(r, 100)
    
    def test_payment_expensive_lunch_sufficient_lunches_sold_increases(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_payment_cheap_lunch_insufficient_money_increases(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_payment_cheap_lunch_insufficient_correct_change(self):
        r=self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(r, 200)
    
    def test_payment_cheap_lunch_insufficient_lunches_sold_increases(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_payment_expensive_lunch_insufficient_money_increases(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_payment_expensive_lunch_insufficient_correct_change(self):
        r=self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(r, 200)
    
    def test_payment_expensive_lunch_insufficient_lunches_sold_increases(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_sufficient_card_purchase_cheap_lunch_amount_debited(self):
        kortti=Maksukortti(300)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 0.60 euroa")
    
    def test_sufficient_card_purchase_cheap_lunch_returns_True(self):
        kortti=Maksukortti(300)
        self.assertEqual(bool(self.kassapaate.syo_edullisesti_kortilla(kortti)), True)
    
    def test_sufficient_card_purchase_cheap_lunch_lunches_sold_increases(self):
        kortti=Maksukortti(300)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_sufficient_card_purchase_expensive_lunch_amount_debited(self):
        kortti=Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
    
    def test_sufficient_card_purchase_expensive_lunch_returns_True(self):
        kortti=Maksukortti(500)
        self.assertEqual(bool(self.kassapaate.syo_maukkaasti_kortilla(kortti)), True)
    
    def test_sufficient_card_purchase_expensive_lunch_lunches_sold_increases(self):
        kortti=Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_cheap_lunch_cashregister_money_unchanged(self):
        kortti=Maksukortti(500)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_expensive_lunch_cashregister_money_unchanged(self):
        kortti=Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_insufficient_card_purchase_cheap_lunch_nothing_debited(self):
        kortti=Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
    
    def test_insufficient_card_purchase_cheap_lunch_returns_False(self):
        kortti=Maksukortti(200)
        self.assertEqual(bool(self.kassapaate.syo_edullisesti_kortilla(kortti)), False)
    
    def test_insufficient_card_purchase_cheap_lunch_lunches_sold_unchanged(self):
        kortti=Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_insufficient_card_purchase_expensive_lunch_nothing_debited(self):
        kortti=Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
    
    def test_insufficient_card_purchase_expensive_lunch_returns_False(self):
        kortti=Maksukortti(200)
        self.assertEqual(bool(self.kassapaate.syo_maukkaasti_kortilla(kortti)), False)
    
    def test_insufficient_card_purchase_expensive_lunch_lunches_sold_unchanged(self):
        kortti=Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_loading_money_onto_card_balance_changes(self):
        kortti=Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, 200)
        self.assertEqual(str(kortti), "Kortilla on rahaa 3.00 euroa")
    
    def test_loading_money_onto_card_cashregister_balance_increases(self):
        kortti=Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)
    
    def test_loading_money_onto_card_invalid_amount_returns(self):
        kortti=Maksukortti(100)
        r=self.kassapaate.lataa_rahaa_kortille(kortti, -1)
        self.assertEqual(r, None)