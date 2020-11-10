import unittest
from HW03_Neil_Gupte import Fraction

""" Unit Test Class """
class Fraction_Test(unittest.TestCase):
    """unit test function to check + working"""
    def test_plus(self)->None:
        a:Fraction=Fraction(1,2)
        b:Fraction=Fraction(1,3)
        res:Fraction=Fraction(5,6)
        self.assertEqual(a+b,res)
        """negative test"""
        self.assertNotEqual(Fraction(1,2)+Fraction(-1,1),Fraction(1,2))
        self.assertEqual(Fraction(2, 4) + Fraction(2, 4), Fraction(8, 8))
        self.assertEqual(Fraction(100, 50) + Fraction(1, 2), Fraction(250, 100))
        self.assertEqual(Fraction(-2, 4) + Fraction(-10, 4), Fraction(-12, 4))

    """unit test function to check - working"""
    def test_minus(self)->None:
        a:Fraction=Fraction(1,2)
        b:Fraction=Fraction(1,2)
        res:Fraction=Fraction(0,4)
        self.assertEqual(a-b,res)
        """negative test"""
        self.assertNotEqual(Fraction(1, 2) - Fraction(-1, 1), Fraction(4, 2))
        self.assertEqual(Fraction(1, 2) - Fraction(-1, 1), Fraction(3, 2))
        self.assertEqual(Fraction(2, 4) - Fraction(2, 4), Fraction(0, 1))
        self.assertEqual(Fraction(100, 50) - Fraction(1, 2), Fraction(150, 100))
        self.assertEqual(Fraction(-2, 4) - Fraction(-10, 4), Fraction(8, 4))

    """unit test function to check * working"""
    def test_times(self)->None:
        a:Fraction=Fraction(1,2)
        b:Fraction=Fraction(1,2)
        res:Fraction=Fraction(1,4)
        self.assertEqual(a*b,res)
        """negative test"""
        self.assertNotEqual(Fraction(1, 2) * Fraction(-1, 1), Fraction(4, 2))
        self.assertEqual(Fraction(1, 2) * Fraction(-1, 1), Fraction(-1, 2))
        self.assertEqual(Fraction(2, 4) * Fraction(2, 4), Fraction(4, 16))
        self.assertEqual(Fraction(100, 50) * Fraction(1, 2), Fraction(100, 100))
        self.assertEqual(Fraction(-2, 4) * Fraction(-10, 4), Fraction(20, 16))

    """unit test function to check / working"""
    def test_div(self)->None:
        a:Fraction=Fraction(4,2)
        b:Fraction=Fraction(1,2)
        res:Fraction=Fraction(8,2)
        self.assertEqual(a/b,res)
        """negative test"""
        self.assertNotEqual(Fraction(1, 2) / Fraction(-1, 1), Fraction(4, 2))
        self.assertEqual(Fraction(1, 2) / Fraction(-1, 1), Fraction(-1, 2))
        self.assertEqual(Fraction(2, 4) / Fraction(2, 4), Fraction(1, 1))
        self.assertEqual(Fraction(100, 50) / Fraction(1, 2), Fraction(200, 50))
        self.assertEqual(Fraction(-2, 4) / Fraction(-10, 4), Fraction(-8, -40))

    """unit test function to check == working"""
    def test_equal(self)->None:
        a:Fraction=Fraction(1,2)
        b:Fraction=Fraction(2,4)
        res:bool=True
        self.assertEqual(a==b,res)
        """negative test"""
        self.assertNotEqual(Fraction(1, 2) == Fraction(-1, 1), True)
        self.assertEqual(Fraction(0, 2) == Fraction(0, 3),  True)
        self.assertEqual(Fraction(-2, 4) == Fraction(-2, 4), True)
        self.assertEqual(Fraction(100, 50) == Fraction(1, 2), False)
        self.assertEqual(Fraction(-10,4) == Fraction(-10, -4), False)

    """unit test function to check != working"""
    def test_not_equal(self)->None:
        a:Fraction=Fraction(1,2)
        b:Fraction=Fraction(3,4)
        res:bool=True
        self.assertEqual(a!=b,res)
        """negative test"""
        self.assertNotEqual(Fraction(1, 2) != Fraction(-1, 1), False)
        self.assertEqual(Fraction(0, 2) != Fraction(0, 3), False)
        self.assertEqual(Fraction(-2, 4) != Fraction(2, 4), True)
        self.assertEqual(Fraction(100, 50) != Fraction(1, 2), True)
        self.assertEqual(Fraction(-10, -4) != Fraction(-10, -4), False)

    """unit test function to check < working"""
    def test_less_than(self)->None:
        a:Fraction=Fraction(1,3)
        b:Fraction=Fraction(1,2)
        res:bool=True
        self.assertEqual(a<b,res)
        """negative test"""
        self.assertNotEqual(Fraction(1, 2) < Fraction(-1, 1), True)
        self.assertEqual(Fraction(0, 2) < Fraction(0, 3), False)
        self.assertEqual(Fraction(-2, 4) < Fraction(2, 4), True)
        self.assertEqual(Fraction(100, 50) < Fraction(200, 2), True)
        self.assertEqual(Fraction(-10, -4) < Fraction(-10, -4), False)

    """unit test function to check <= working"""
    def test_less_equal(self)->None:
        a:Fraction=Fraction(1,3)
        b:Fraction=Fraction(1,2)
        res:bool=True
        self.assertEqual(a<=b,res)
        """negative test"""
        self.assertNotEqual(Fraction(1, 2) <= Fraction(-1, 1), True)
        self.assertEqual(Fraction(0, 2) <= Fraction(0, 3), True)
        self.assertEqual(Fraction(-2, 4) <= Fraction(2, 4), True)
        self.assertEqual(Fraction(100, 50) <= Fraction(1, 2), False)
        self.assertEqual(Fraction(10,4) <= Fraction(10,2), True)

    """unit test function to check > working"""
    def test_greater_than(self)->None:
        a:Fraction=Fraction(1,2)
        b:Fraction=Fraction(1,3)
        res:bool=True
        self.assertEqual(a>b,res)
        """negative test"""
        self.assertNotEqual(Fraction(1, 2) > Fraction(-1, 1), False)
        self.assertEqual(Fraction(0, 2) > Fraction(0, 3), False)
        self.assertEqual(Fraction(-2, -4) > Fraction(2,-4), True)
        self.assertEqual(Fraction(100, 50) > Fraction(1, 2), True)
        self.assertEqual(Fraction(-10, -4) > Fraction(-10, -4), False)

    """unit test function to check >= working"""
    def test_greater_equal(self)->None:
        a:Fraction=Fraction(1,1)
        b:Fraction=Fraction(1,2)
        res:bool=True
        self.assertEqual(a>=b,res)
        """negative test"""
        self.assertNotEqual(Fraction(1, 2) >= Fraction(-1, 1), False)
        self.assertEqual(Fraction(0, 2) >= Fraction(0, 3), True)
        self.assertEqual(Fraction(-2, 4) >= Fraction(2, 4), False)
        self.assertEqual(Fraction(100, 50) >= Fraction(200, 100), True)
        self.assertEqual(Fraction(10, 4) >= Fraction(10, 3), False)

    """unit test function to check if proper str is returned from Fraction"""
    def test_check_str(self)->None:
        a:Fraction=Fraction(1,3)
        b:str="1/3"
        self.assertEqual(str(a),b)
        self.assertEqual(str(Fraction(1,4)),"1/4")
        """negative test"""
        self.assertNotEqual(str(Fraction(-1, -2)),"1/2")
        self.assertEqual(str(Fraction(-2, -4)), "-2/-4")
        self.assertEqual(str(Fraction(100, 2)), "100/2")
        self.assertEqual(str(Fraction(-90, 4)), "-90/4")

    """unit test function to check if Value error is Raised when 0 is passed as denominator"""
    def test_denomzero(self)->None:
        self.assertRaises(ValueError,Fraction,1,0)
        self.assertRaises(ValueError, Fraction, 200, 0)
        self.assertRaises(ValueError, Fraction, 0, 0)
        self.assertRaises(ValueError, Fraction, -1, -0)



if __name__=='__main__':
    unittest.main(exit=False,verbosity=2)