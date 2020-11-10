import unittest
from HW06_Neil_Gupte import HW06,DonutQueue
from typing import *

class ListCopyTest(unittest.TestCase):
    """ test list copy function """
    def test_list_copy(self)->None:
        a:List[Any]=[1,2,3,4]
        b:List[Any]=HW06.list_copy(a)
        self.assertEqual(a,b)
        self.assertEqual(HW06.list_copy([]), [])
        self.assertEqual(HW06.list_copy(['a','b','c']), ['a','b','c'])
        self.assertEqual(HW06.list_copy(['a', 'b', 1]), ['a', 'b', 1])
        self.assertEqual(HW06.list_copy(['a', 'b',-10,-20]), ['a', 'b',-10,-20])

class List_Intersect_Test(unittest.TestCase):
    """ test list intersect function """
    def test_list_intersect(self)->None:
        a:List[Any]=[1,2,3,4]
        b: List[Any] = [2,3,4]
        c:List[Any]=HW06.list_intersect(a,b)
        self.assertEqual(c,[2,3,4])
        self.assertEqual(HW06.list_intersect(['a',1,'b'],[1]), [1])
        self.assertEqual(HW06.list_intersect([],[]), [])
        self.assertEqual(HW06.list_intersect(["apple","pear","guava"], ["apple","pear","guava"]), ["apple","pear","guava"])
        self.assertEqual(HW06.list_intersect(["apple","pear",-10,-20], ["apple","pear"]), ["apple","pear"])
        self.assertEqual(HW06.list_intersect(["apple", "pear", -10, -20], ["apple", "pear",-20]), ["apple", "pear",-20])



class List_Difference_Test(unittest.TestCase):
    """ test list difference function """
    def test_list_difference(self)->None:
        a:List[Any]=[1,2,3,4]
        b: List[Any] = [2,3,4]
        c:List[Any]=HW06.list_difference(a,b)
        self.assertEqual(c,[1])
        self.assertEqual(HW06.list_difference(['a',1,'b'],[1]), ['a','b'])
        self.assertEqual(HW06.list_difference([],[]), [])
        self.assertEqual(HW06.list_difference(["apple","pear","guava","papaya"], ["apple","pear","guava"]), ["papaya"])
        self.assertEqual(HW06.list_difference(["apple","pear","guava","papaya",2,5], ["apple","pear","guava"]), ["papaya",2,5])
        self.assertEqual(HW06.list_difference(['a','b','c'], ["d"]), ['a','b','c'])



class Remove_Vowels_Test(unittest.TestCase):
    """ test remove vowels function """
    def test_remove_vowels(self)->None:
        a:str="Amy is my favorite daughter"
        b:str=HW06.remove_vowels(a)
        c:str="my favorite daughter"
        self.assertEqual(b,c)
        self.assertEqual(HW06.remove_vowels("12345"),"12345")
        self.assertEqual(HW06.remove_vowels("12345 is an apple"), "12345")
        self.assertEqual(HW06.remove_vowels("Dont Go For this"), "Dont Go For this")
        self.assertEqual(HW06.remove_vowels("I am a simple mAn"), "simple mAn")
        self.assertEqual(HW06.remove_vowels(""), "")

class Password_Check_Test(unittest.TestCase):
    """ test check password function """
    def test_check_pwd(self)->None:
        a:str="2ABc"
        b:bool=HW06.check_pwd(a)
        self.assertEqual(b,True)
        self.assertEqual(HW06.check_pwd("12345"),False)
        self.assertEqual(HW06.check_pwd(""),False)
        self.assertEqual(HW06.check_pwd("A1223bcA"),False)
        self.assertEqual(HW06.check_pwd("1AEccccc"),True)
        self.assertEqual(HW06.check_pwd("1     abAB"), True)



class DonutQueueTest(unittest.TestCase):
    "test donut queue function"
    def test_queue(self):
        dq = DonutQueue()
        self.assertIsNone(dq.next_customer())
        dq.arrive("Sujit", False)
        dq.arrive("Fei", False)
        dq.arrive("Prof JR", True)
        self.assertEqual(dq.waiting(), "Prof JR, Sujit, Fei")
        dq.arrive("Nanda", True)
        self.assertEqual(dq.waiting(), "Prof JR, Nanda, Sujit, Fei")
        self.assertEqual(dq.next_customer(), "Prof JR")
        self.assertEqual(dq.next_customer(), "Nanda")
        self.assertEqual(dq.next_customer(), "Sujit")
        self.assertEqual(dq.waiting(), "Fei")
        self.assertEqual(dq.next_customer(), "Fei")
        self.assertIsNone(dq.next_customer())
        df=DonutQueue()
        df.arrive("Gru", False)
        df.arrive("Brutus",True)
        df.arrive("Hercules", True)
        self.assertEqual(df.waiting(), "Brutus, Hercules, Gru")
        self.assertEqual(df.next_customer(), "Brutus")
        self.assertEqual(df.next_customer(), "Hercules")
        self.assertEqual(df.waiting(),  "Gru")
        df.next_customer()
        self.assertIsNone(df.next_customer())

class Reorder_Test(unittest.TestCase):
    """ test reorder function """
    def test_reorder(self)->None:
        a:List[Any]=['c','b','a']
        b:List[Any]=HW06.reorder(a)
        c:List[Any]=['a','b','c']
        self.assertEqual(HW06.reorder([10,1,5,3]),[1,3,5,10])
        self.assertEqual(HW06.reorder([-10,-1,-5,-3]),[-10,-5,-3,-1])
        self.assertEqual(HW06.reorder([]), [])
        self.assertEqual(HW06.reorder(['e','b','a']), ['a','b','e'])
        self.assertEqual(HW06.check_pwd(""),False)
        self.assertEqual(HW06.check_pwd("A1223bcA"),False)
        self.assertEqual(HW06.check_pwd("1AEccccc"),True)
        self.assertEqual(HW06.check_pwd("1     abAB"), True)






if __name__=='__main__':
    unittest.main(exit=False,verbosity=2)
