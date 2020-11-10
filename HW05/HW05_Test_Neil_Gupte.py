import unittest
from HW05_Neil_Gupte import HW05
from typing import *


""" Unit Test Class """
class ReverseTest(unittest.TestCase):
    """ test reverse function """
    def test_reverse(self)->None:
        string:str= 'Stars'
        rev:str="sratS"
        check_rev:str=HW05.reverse(string)
        self.assertEqual(rev,check_rev)
        self.assertEqual('Madam', HW05.reverse('madaM'))
        self.assertEqual('00001', HW05.reverse('10000'))
        self.assertEqual('', HW05.reverse(''))
        # self.assertRaises(ValueError, HW05.reverse,2)


class SubstringTest(unittest.TestCase):
    """ test substring function """
    def test_substring(self)->None:
        string:str= 'Stars'
        target:str="rs"
        offset:int=HW05.substring(target,string)
        self.assertEqual(offset,3)
        self.assertEqual(HW05.substring('ppi','Mississippi'),8)
        self.assertEqual(HW05.substring('',''),0)
        self.assertEqual(HW05.substring('xx','ppqqp'),-1)
        # self.assertRaises(ValueError, HW05.substring,2,'abc')



class FindSecondTest(unittest.TestCase):
    """ test find_second function """
    def test_find_second(self)->None:
        string:str= 'posopop'
        target:str="op"
        offset:int=HW05.find_second(target,string)
        self.assertEqual(offset,5)
        self.assertEqual(HW05.find_second('',''),-1)
        self.assertEqual(HW05.find_second('l','hello'),3)
        self.assertEqual(HW05.find_second('hello','hello'),-1)
        self.assertEqual(HW05.find_second('abba', 'abbabba'), 3)
        self.assertEqual(HW05.find_second('abbaa', 'abba'), -1)
        # self.assertRaises(ValueError,HW05.find_second,2,'abc')

class GetLinesTest(unittest.TestCase):
    """ test get_lines function """
    def test_get_lines(self)->None:
        file_name = 'check.txt'


        expect: List[str] = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>','<line4.1 line4.2>', '<line5>', '<line6>']
        result: List[str] = list(HW05.get_lines(file_name))
        self.assertEqual(result, expect)
        #self.assertRaises(FileNotFoundError,HW05.get_lines,file_name)








if __name__=='__main__':
    unittest.main(exit=False,verbosity=2)
