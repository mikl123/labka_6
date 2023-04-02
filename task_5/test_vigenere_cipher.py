"""
Tests for square
"""
import unittest

from vigenere_cipher import VigenereCipher

class ClassesTest(unittest.TestCase):
    """
    Test for Vehicle class
    """
    def test_ciphre(self):
        """
        Test for ciphre
        """
        # Train Key word
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODEDINPYTHON")
        self.assertEqual( encoded , "XECWQXUIVCRKHWA")
        decoded=cipher.decode(encoded)
        self.assertEqual( decoded , "ENCODEDINPYTHON")
    def test_lower_case(self):
        """
        Test lowercase
        """
        cipher = VigenereCipher("Happy")
        encoded = cipher.encode("ENCODEDINPYTHON")
        self.assertEqual( encoded , "LNRDBLDXCNFTWDL")
        decoded=cipher.decode(encoded)
        print(decoded)
        self.assertEqual( decoded , "ENCODEDINPYTHON")
    def test_spaces(self):
        """
        Test spaces
        """
        cipher = VigenereCipher("Happy")
        encoded = cipher.encode("EN CODE DIN PYTHON")
        self.assertEqual( encoded , "LNRDBLDXCNFTWDL")
        decoded=cipher.decode(encoded)
        print(decoded)
        self.assertEqual( decoded , "ENCODEDINPYTHON")
    def test_expand_word(self):
        """
        Test spaces
        """
        cipher = VigenereCipher("Happy")
        self.assertEqual(cipher.extend_keyword(1),"H")
        self.assertEqual(cipher.extend_keyword(10),"HAPPYHAPPY")
    def test_expand_word(self):
        """
        Test spaces
        """
        cipher = VigenereCipher("Happy")
        self.assertEqual(cipher.extend_keyword(1),"H")
        self.assertEqual(cipher.extend_keyword(10),"HAPPYHAPPY")
    def test_combine_letters(self):
        """
        Combine letters
        """
        cipher = VigenereCipher("Happy")
        self.assertEqual( cipher.combine_character("E", "T") , "X")
        self.assertEqual( cipher.combine_character("N", "R") , "E")
    def test_separate_character(self):
        """
        Test separation
        """
        cipher = VigenereCipher("Happy")
        self.assertEqual( cipher.separate_character("X", "T") , "E")
        self.assertEqual( cipher.separate_character("E", "R") , "N")
unittest.main(argv=[""], verbosity=2, exit=False)
