"""The assignment hw05  focuses on string methods, slices, working with files, and automated testing"""

from typing import *


class HW05:
    """class for calling all the functions"""
    def reverse(s: str) -> str:
        """function to reverse the given string using while loop """

        # if type(s)!= str:
        #     raise ValueError("Please check that a string is passed")

        rev_str:str=""
        cnt:int=len(s)-1
        while cnt>=0:
            rev_str+=s[cnt]
            cnt-=1
        return rev_str


    def substring(target: str, s: str) -> int:
        """custom method which mimics find method of python"""

        # if type(s)!= str or type(target)!= str:
        #     raise ValueError("Please check that a string is passed")

        if len(target)>len(s):
            return -1
        if len(target)==len(s)==0:
            return 0
        len_tar:int=len(target)
        len_s: int = len(s)
        for i in range(len_s):
            if s[i:i+len_tar]==target:
                return i
        return -1


    def find_second(target: str, string: str) -> int:

        """function to return the index of second occurrence of target inside a string print -1 instead """

        # if type(string)!= str or type(target)!= str:
        #     raise ValueError("Please check that a string is passed")
        # first:int=HW05.substring(target,string)
        # if first==-1:
        #     return first
        # len_tar: int = len(target)
        # len_string: int = len(string)
        # for i in range(first+1,len_string):
        #     if string[i:i+len_tar]==target:
        #         return i
        # return -1

        return string.find(target, string.find(target) + 1)

    def get_lines(path: str) -> Iterator[str]:
        """A generator which returns that opens a file for reading and returns one line from the file at a time"""


        try:
            fp:IO[AnyStr]=open(path,'r')
        except FileNotFoundError:
            raise FileNotFoundError("Please check the filepath ")
        else:
            lines:List[str]=fp.readlines()

            """first join all elements into one string , replace backslash + \n with empty and 
             then create generate the list back splitting on \n"""

            lines = "".join(lines).replace("\\\n", "").splitlines()

            for line in lines:
                check:int=line.find('#')
                if check ==-1:
                    yield line
                elif check==0:
                    continue
                else:
                    yield line[:check]

"""main function to check generator """
# def main() -> None:
#     file_name = 'check.txt'
#
#     for line in HW05.get_lines(file_name):
#         print(line)
# main()
#

