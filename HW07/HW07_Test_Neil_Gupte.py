import unittest
from HW07_Neil_Gupte import HW07

from typing import *
class AnagramListTest(unittest.TestCase):
    """ test anagram list function"""
    def test_anagram_list(self)->None:
        a:str="hello"
        b:str="loleh"
        self.assertEqual(HW07.anagrams_lst(a,b),True)
        self.assertEqual(HW07.anagrams_lst("", ""), True)
        self.assertEqual(HW07.anagrams_lst("yup", "yu"), False)
        self.assertEqual(HW07.anagrams_lst("12345", "123"), False)
        self.assertEqual(HW07.anagrams_lst("12345", "12345"), True)

class AnagramDictTest(unittest.TestCase):
    """ test anagram dictionary function"""
    def test_anagram_dict(self)->None:
        a:str="hello"
        b:str="loleh"
        self.assertEqual(HW07.anagrams_dd(a,b),True)
        self.assertEqual(HW07.anagrams_dd("", ""), True)
        self.assertEqual(HW07.anagrams_dd("yup", "yu"), False)
        self.assertEqual(HW07.anagrams_dd("12345", "123"), False)
        self.assertEqual(HW07.anagrams_dd("12345", "12345"), True)

class AnagramCounterTest(unittest.TestCase):
    """ test anagram counter function"""
    def test_anagram_counter(self)->None:
        a:str="hello"
        b:str="loleh"
        self.assertEqual(HW07.anagrams_cntr(a,b),True)
        self.assertEqual(HW07.anagrams_cntr("", ""), True)
        self.assertEqual(HW07.anagrams_cntr("yup", "yu"), False)
        self.assertEqual(HW07.anagrams_cntr("12345", "123"), False)
        self.assertEqual(HW07.anagrams_cntr("12345", "12345"), True)


class CoversAlphabetTest(unittest.TestCase):
    """ test covers_alphabet function """
    def test_covers_alph(self)->None:
        a:str="AbCdefghiJklomnopqrStuvwxyz"
        self.assertEqual(HW07.covers_alphabet(a),True)
        self.assertEqual(HW07.covers_alphabet("AbCdefghiJklomnopqrStuvwxyz12344"), True)
        self.assertEqual(HW07.covers_alphabet("1bCdefghiJklomnopqrStuvwxz"), False)
        self.assertEqual(HW07.covers_alphabet(""), False)
        self.assertEqual(HW07.covers_alphabet("The quick brown fox jumps over the lazy dog"), True)


class WebAnalyzerTest(unittest.TestCase):
    """ test web_analyzer function """
    def test_web_analyzer(self)->None:

        weblogs: List[Tuple[str, str]] = [
            ('Nanda', 'google.com'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Nanda', 'python.org'),
            ('Fei', 'dzone.com'), ('Nanda', 'google.com'),
            ('Maha', 'google.com'), ]

        weblogs2: List[Tuple[str, str]] = [
            ('Nanda', 'google.com'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Nanda', 'python.org'),
            ('Fei', 'dzone.com'), ('Nanda', 'google.com'),
            ('Maha', 'google.com'),('Anil', 'apple.com'),('zoro', 'zoom.com')]

        weblogs3: List[Tuple[str, str]] = [
            ('Nanda', 'google.com'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Nanda', 'python.org'),
            ('Fei', 'dzone.com'), ('Nanda', 'google.com'),
            ('Maha', 'google.com'), ('Anil', 'apple.com'), ('Zoro', 'apple.com')]

        weblogs4: List[Tuple[str, str]] = [
            ('Nanda', 'zcash.com'),('Manda', 'zcash.com'),('Onda', 'zcash.com')]

        summary: List[Tuple[str, List[str]]] = [
            ('dzone.com', ['Fei']),
            ('google.com', ['Maha', 'Nanda']),
            ('python.org', ['Fei', 'Nanda']), ]


        summary2: List[Tuple[str, List[str]]] = [
            ('apple.com', ['Anil']),
            ('dzone.com', ['Fei']),
            ('google.com', ['Maha', 'Nanda']),
            ('python.org', ['Fei', 'Nanda']),
            ('zoom.com', ['zoro'])]

        summary3: List[Tuple[str, List[str]]] = [
            ('apple.com', ['Anil','Zoro']),
            ('dzone.com', ['Fei']),
            ('google.com', ['Maha', 'Nanda']),
            ('python.org', ['Fei', 'Nanda'])]

        summary4: List[Tuple[str, List[str]]] = [
            ('zcash.com', ['Manda','Nanda','Onda']) ]

        self.assertEqual(HW07.web_analyzer(weblogs), summary)
        self.assertEqual(HW07.web_analyzer(weblogs2), summary2)
        self.assertEqual(HW07.web_analyzer(weblogs3), summary3)
        self.assertEqual(HW07.web_analyzer(weblogs4), summary4)


if __name__=='__main__':
    unittest.main(exit=False,verbosity=2)

