import unittest

from src.utilities.builder import OProgramBuilder
from src.tests.mock_time import MockTimeSpecific
from src.messages import LANGUAGES

class TestPalindrome(unittest.TestCase):

    def setUp(self):
        self.builder = OProgramBuilder().with_language("fr")

    def test_palindrome_palindrome(self):
        oprogram = self.builder.build()
        resultat = oprogram.palindrome("kayak")
        attendu = LANGUAGES["fr"]["felicitation"]
        self.assertIn(attendu, resultat)

    def test_palindrome_vide(self):
        oprogram = self.builder.build()
        resultat = oprogram.palindrome("")
        attendu = LANGUAGES["fr"]["felicitation"]
        self.assertIn(attendu, resultat)

    def test_palindrome_sans_entre(self):
        oprogram = self.builder.build()
        with self.assertRaises(TypeError):
            oprogram.palindrome(None)
        
    def test_palindrome_entre_mauvais_type(self):
        oprogram = self.builder.build()
        with self.assertRaises(TypeError):
            oprogram.palindrome(42)
        
    def test_palindrome_speciaux(self):
        oprogram = self.builder.build()
        resultat = oprogram.palindrome("No#on")
        attendu = LANGUAGES["fr"]["felicitation"]
        self.assertIn(attendu, resultat)

    def test_non_palindrome_speciaux(self):
        oprogram = self.builder.build()
        resultat = oprogram.palindrome("#salut")
        self.assertIn("tulas#", resultat)

    def test_palindrome_casse(self):
        oprogram = self.builder.build()
        resultat = oprogram.palindrome("Level")
        attendu = LANGUAGES["fr"]["felicitation"]
        self.assertIn(attendu, resultat)

    def test_non_palindrome_casse(self):
        oprogram = self.builder.build()
        resultat = oprogram.palindrome("Python")
        self.assertIn("nohtyP", resultat)

    def test_non_palindrome(self):
        oprogram = self.builder.build()
        resultat = oprogram.palindrome("maison")
        self.assertIn("nosiam",resultat)

    def test_non_palindrome_nombre(self):
        oprogram = self.builder.build()
        resultat = oprogram.palindrome("12test")
        self.assertIn("tset21",resultat)

    def test_palindrome_nombre(self):
        oprogram = self.builder.build()
        resultat = oprogram.palindrome("121")
        attendu = LANGUAGES["fr"]["felicitation"]
        self.assertIn(attendu, resultat)

    def test_initialisation_langue(self):
        langue = "en"
        oprogram = self.builder.with_language(langue).build()
        resultat = oprogram.palindrome("check")
        self.assertIsInstance(resultat, str)
        
    def test_goodbye_known_language(self):
        langue = "en"
        oprogram = self.builder.with_language(langue).build()
        resultat = oprogram.palindrome("hello")
        attendu = LANGUAGES[langue]["adieu"]
        self.assertIn(attendu, resultat)

    def test_congratulation_known_language(self):
        langue = "en"
        oprogram = self.builder.with_language(langue).build()
        resultat = oprogram.palindrome("madam")
        attendu = LANGUAGES[langue]["felicitation"]
        self.assertIn(attendu, resultat)

    def test_unknown_language(self):
        langue="klingon"
        with self.assertRaises(ValueError):
            self.builder.with_language(langue).build()

    def test_message_format(self):
        langue = "de"
        oprogram = self.builder.with_language(langue).with_time_provider(MockTimeSpecific(9)).build()
        resultat=oprogram.palindrome("wort")
        self.assertTrue(resultat.startswith(LANGUAGES[langue]["salutation_am"]))
        self.assertTrue(resultat.strip().endswith(LANGUAGES[langue]["adieu"]))

    def test_salutation_morning(self):
        langue = "es"
        oprogram = self.builder.with_language(langue).with_time_provider(MockTimeSpecific(7)).build()
        resultat = oprogram.palindrome("hola")
        attendu = LANGUAGES[langue]["salutation_am"]
        self.assertIn(attendu, resultat)

    def test_salutation_afternoon(self):
        langue = "es"
        oprogram = self.builder.with_language(langue).with_time_provider(MockTimeSpecific(16)).build()
        resultat = oprogram.palindrome("adios")
        attendu = LANGUAGES[langue]["salutation_pm"]
        self.assertIn(attendu, resultat)

    def test_salutation_night(self):
        langue = "es"
        oprogram = self.builder.with_language(langue).with_time_provider(MockTimeSpecific(21)).build()
        resultat = oprogram.palindrome("noche")
        attendu = LANGUAGES[langue]["salutation_nuit"]
        self.assertIn(attendu, resultat)

    def test_salutation_morning_boundary(self):
        langue = "de"
        oprogram = self.builder.with_language(langue).with_time_provider(MockTimeSpecific(4)).build()
        resultat = oprogram.palindrome("test")
        attendu = LANGUAGES[langue]["salutation_am"]
        self.assertIn(attendu, resultat)

    def test_salutation_afternoon_boundary(self):
        langue = "de"
        oprogram = self.builder.with_language(langue).with_time_provider(MockTimeSpecific(12)).build()
        resultat = oprogram.palindrome("test")
        attendu = LANGUAGES[langue]["salutation_pm"]
        self.assertIn(attendu, resultat)

    def test_salutation_night_boundary(self):
        langue = "de"
        oprogram = self.builder.with_language(langue).with_time_provider(MockTimeSpecific(20)).build()
        resultat = oprogram.palindrome("test")
        attendu = LANGUAGES[langue]["salutation_nuit"]
        self.assertIn(attendu, resultat)

    def test_state_unchanged(self):
        langue = "fr"
        oprogram = self.builder.build()
        old_messages = oprogram.messages.copy()
        oprogram.palindrome("civic")
        self.assertEqual(oprogram.messages, old_messages)