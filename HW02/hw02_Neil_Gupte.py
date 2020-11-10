"""Fraction Calculator to carry out arithmetic operations on two fractions
along with a function to test the results """



class Fraction:
    """initializer where we set the numerator and the denominator and raise Valueerror if denom is equal to zero """
    def __init__(self,numerator,denominator)->str:
        self.numerator=numerator
        self.denominator=denominator

        if denominator==0:
            raise ValueError("Please dont use 0 as denominator")
        if numerator==0:
            denominator=1

    """This method handles addition of two fractions"""
    def plus(self,other:"Fraction")-> "Fraction":
        plus_num:float=self.numerator *other.denominator + self.denominator * other.numerator
        plus_den:float=self.denominator * other.denominator
        return Fraction(plus_num,plus_den)
    """This method handles the subtraction of two fractions """
    def minus(self, other:'Fraction') -> 'Fraction':
        minus_num:float = self.numerator * other.denominator - self.denominator * other.numerator
        minus_den:float = self.denominator * other.denominator
        return Fraction(minus_num, minus_den)

    """This method handles the multiplication of two fractions """
    def times(self,other:'Fraction')-> 'Fraction':
        times_num:float=self.numerator * other.numerator
        times_den:float=self.denominator * other.denominator
        return Fraction(times_num,times_den)

    """This method handles the division of two fractions """
    def divide(self,other:'Fraction')-> 'Fraction':
        divide_num:float=self.numerator * other.denominator
        divide_den:float=self.denominator * other.numerator
        return Fraction(divide_num,divide_den)

    """This method handles the subtraction of two fractions """
    def equal(self,other:'Fraction')-> bool:
        return (self.numerator * other.denominator) == (self.denominator * other.numerator)

    """This method return a string to represent the Fraction"""
    def __str__(self)->str:
        return str(self.numerator)+"/"+str(self.denominator)


"""Class for setting operands, operator and calling functions from Fractions"""
class Calculator:
    """We set both the operands to be 0/1 initially"""
    def __init__(self):
        self.op1= Fraction(0,1)
        self.op2= Fraction(0,1)
        self.operator=None
        self.result=Fraction(0,1)

    """set the operand 1 as our first fraction"""
    def set_op1(self,op1:"Fraction")->None:
        self.op1=op1
    """set the operand 2 as our second fraction"""
    def set_op2(self,op2:"Fraction")->None:
        self.op2=op2
    """we check what operator is passed and depending upon that call the appropriate method from Fractions"""
    def operation(self,operator:str):
        if operator=='+':
            return self.op1.plus(self.op2)
        elif operator=='-':
            return self.op1.minus(self.op2)
        elif operator=='*':
            return self.op1.times(self.op2)
        elif operator=='/':
            return self.op1.divide(self.op2)
        else:
            return self.op1.equal(self.op2)

"""function to accept proper operator from the user """
def operator_choice()->str :
    while True:
        check_list:str = ['+','-','/','*','=']
        user_input:str= input(str("""\nPlease type the arithmetic operator \n + To add fractions \n - To subtract fractions\n * to multiply fractions \n / to divide fractions \n = to check if two fractions are equal\n\n"""))
        if user_input in check_list:
            return user_input

"""function to accept numerator and denominnator of first fraction.We have used try and except to check for invalid inputs"""
def fraction_one()->"Fraction":
    while True:
        try:
            num1: float = float(input(("\nPlease input the numerator for first fraction")))
            den1: float = float(input(("\nPlease input the denominator for first fraction")))
        except ValueError:
            print("\n Please enter only numeric input")
            continue
        f1:Fraction=Fraction(num1,den1)
        print(f"\nThe first fraction chosen is {f1} ")
        return f1

"""function to accept numerator and denominnator of second fraction.We have used try and except to check for invalid inputs"""
def fraction_two()->"Fraction":
    while True:
        try:
            num1: float = float(input(("\nPlease input the numerator for second fraction")))
            den1: float = float(input(("\nPlease input the denominator for second fraction")))
        except ValueError:
            print("\n Please enter only numeric input")
            continue
        f2:Fraction=Fraction(num1,den1)
        print(f"\nThe second fraction chosen is {f2} ")
        return f2

"""function to check our test cases for each operator"""
def test_suite():
    # + test
    res1=Fraction(1,2).plus(Fraction(1,3))
    assert (res1.numerator==5 and res1.denominator==6)

    # - test
    res2= Fraction(1,4).minus(Fraction(1,2))
    assert (res2.numerator==-2 and res2.denominator==8)

    # / test
    res3= Fraction(2,3).divide(Fraction(1,4))
    assert (res3.numerator==8 and res3.denominator==3)

    # * test
    res4= Fraction(1,4).times(Fraction(3,7))
    assert (res4.numerator==3 and res4.denominator==28)

    # 3 plus in one operation
    res5=Fraction(1,2).plus(Fraction(3,4)).plus(Fraction(4,4))
    assert (res5.numerator==72 and res5.denominator==32)

    # = test
    res6=Fraction(1,6).equal(Fraction(2,12))
    assert (res6==True)


"""main function where we call all other functions from Fractions and Calculator class"""
def main():
    test_suite()
    print("\n\n---------------Python Fraction Calculator---------------")
    f1:Fraction=fraction_one()
    f2:Fraction=fraction_two()
    op:str=operator_choice()
    calc:Calculator = Calculator()
    calc.set_op1(f1)
    calc.set_op2(f2)
    result:Fraction=calc.operation(op)
    print(f"\n The Final Result is \n\n {f1} {op} {f2} = {result}")
    print(f"----------------------------------------------------------------------------------------")



if __name__ == '__main__':
     main()