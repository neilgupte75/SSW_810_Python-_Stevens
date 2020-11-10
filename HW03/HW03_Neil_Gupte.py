"""same fraction class from previous assignment with more relational operators added and dunder functions created ="""



class Fraction:
    """initializer where we set the numerator and the denominator and raise Valueerror if denom is equal to zero """
    def __init__(self,numerator:float,denominator:float)->str:
        self.numerator:float=numerator
        self.denominator:float=denominator

        if denominator==0:
            raise ValueError("Please dont use 0 as denominator")
        if numerator==0:
            denominator=1

    """This method handles addition of two fractions"""
    def __add__(self,other:"Fraction")-> "Fraction":
        plus_num:float=self.numerator *other.denominator + self.denominator * other.numerator
        plus_den:float=self.denominator * other.denominator
        return Fraction(plus_num,plus_den)
    """This method handles the subtraction of two fractions """
    def __sub__(self, other:'Fraction') -> 'Fraction':
        minus_num:float = self.numerator * other.denominator - self.denominator * other.numerator
        minus_den:float = self.denominator * other.denominator
        return Fraction(minus_num, minus_den)

    """This method handles the multiplication of two fractions """
    def __mul__(self,other:'Fraction')-> 'Fraction':
        times_num:float=self.numerator * other.numerator
        times_den:float=self.denominator * other.denominator
        return Fraction(times_num,times_den)

    """This method handles the division of two fractions """
    def __truediv__(self,other:'Fraction')-> 'Fraction':
        divide_num:float=self.numerator * other.denominator
        divide_den:float=self.denominator * other.numerator
        return Fraction(divide_num,divide_den)

    """This method checks if two fractions are equal """
    def __eq__(self,other:'Fraction')-> bool:
        return (self.numerator * other.denominator) == (self.denominator * other.numerator)

    """This method checks if two fractions are not equal """

    def __ne__(self, other: 'Fraction') -> bool:
        return not self==other

    """This method checks if one fraction is less than the other """

    def __lt__(self, other: 'Fraction') -> bool:
        return (self.numerator * other.denominator) < (self.denominator * other.numerator)

    """This method checks if one fraction is less than or equal to the other  """

    def __le__(self, other: 'Fraction') -> bool:
        return not other < self

    """This method checks if one fraction is greater than the other  """

    def __gt__(self, other: 'Fraction') -> bool:
        return other<self

    """This method checks if one fraction is greater than or equal to the other """

    def __ge__(self, other: 'Fraction') -> bool:
        return not other > self

    """This method return a string to represent the Fraction"""
    def __str__(self)->str:
        return str(self.numerator)+"/"+str(self.denominator)



