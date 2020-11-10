import unittest
from HW04_Neil_Gupte import count_vowels
from HW04_Neil_Gupte import last_occurrence
from HW04_Neil_Gupte import my_enumerate
from HW04_Neil_Gupte import random_integer_generator,find_target
from typing import *

class CountVowelsTest(unittest.TestCase):
    """unit test function to check if countvowels return correct number of vowels"""
    def test_count_vowels(self) -> None:
        a:str="people we are"
        b:int=count_vowels(a)
        self.assertEqual(b, 6)
        self.assertEqual(count_vowels('hello world'), 3)
        self.assertEqual(count_vowels('one two three'), 5)
        self.assertEqual(count_vowels('22222luke I am your father11111'), 8)
        self.assertEqual(count_vowels('-2020zzzzzzzz'), 0)

class FindLastTest(unittest.TestCase):
    """unit test function to check if proper last occurence is returned"""
    def test_last_occurence(self) -> None:
        a:List[str]=['apple','guava','kiwi','21','kiwi']
        b:str="kiwi"
        c:Optional[int]=last_occurrence(b,a)
        self.assertEqual(c, 4)
        self.assertEqual(last_occurrence("p","apple"), 2)
        self.assertEqual(last_occurrence(0,[1,2,2,3,3,3]), None)
        self.assertEqual(last_occurrence(-1,[1,1,1,1,1,-1,-1,-2]), 6)
        self.assertEqual(last_occurrence('kiwi',['apple','guava','kiwi','21','kiwi']), 4)

class EnumerateTest(unittest.TestCase):
    """unit test function to check if the generator created mimics enumerate"""
    def test_my_enumerate(self) -> None:
        a:List[str]=['apple','guava','kiwi','21','kiwi']
        b:Iterator[Any]=my_enumerate(a)

        self.assertEqual(list(b),list(enumerate(a)))
        self.assertEqual(list(my_enumerate(["12a",'12v','21s','31'])), list(enumerate(["12a",'12v','21s','31'])))
        self.assertEqual(list(my_enumerate("apples")), list(enumerate("apples")))
        self.assertEqual(list(my_enumerate((1,2,3,5,6,6))), list(enumerate((1,2,3,5,6,6))))
        self.assertEqual(list(my_enumerate(["12",12,"12"])), list(enumerate(["12",12,"12"])))


class FindTargetTest(unittest.TestCase):
    """unit test function to check the functioning of find_target"""
    def test_find_target(self) -> None:
        self.assertEqual(find_target(3, 3, 3, 1), 1)
        self.assertEqual(find_target(3, 3, 3, 100), 1)
        self.assertEqual(find_target(10, 10, 10, 1), 1)
        self.assertRaises(ValueError, find_target, 10, 11,12,2)
        self.assertRaises(ValueError, find_target, 10, 12, 5, 2)
        self.assertRaises(ValueError, find_target, 13, 12, 15, 0)



if __name__=='__main__':
    unittest.main(exit=False,verbosity=2)