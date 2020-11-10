
"""Hw 06 program where we practice list comprehension"""
from typing import *


class HW06:
    def list_copy(l: List[Any]) -> List[Any]:
            """Function to return copy of the list"""
            return [item for item in l]

    def list_intersect(l1: List[Any], l2: List[Any]) -> List[Any]:
        """Function to find intersection between 2 lists"""
        return [item for item in l1 if item in l2]

    def list_difference(l1: List[Any], l2: List[Any]) -> List[Any]:
        """Function to find the difference between two lists"""
        return [item for item in l1 if item not in l2]

    def remove_vowels(string: str) -> str:
        """Function which returns the words in string which do not start with vowels"""
        return " ".join([item for item in string.split() if not item.lower().startswith(("a","e","i","o","u"))])

    def check_pwd(password: str) -> bool:
        """Function to check if the password str satisfies the given criterion  """
        return len(password) >= 4 and sum([1 for item in password if item.isupper()]) >= 2 \
               and sum([1 for item in password if item.islower()]) >= 1 \
               and password[0].isdigit()

    def reorder(l: List[Any]) -> List[Any]:
        """Function to return a sorted copy of the list """
        reorder_list:List[Any]=[]
        for item in l:
            i:int=len(reorder_list)-1
            while i>=0:
                if item >= reorder_list[i]:
                    reorder_list.insert(i + 1, item)
                    break
                i-=1
            else:
                reorder_list.insert(0, item)

        return reorder_list







class DonutQueue:
    """Class for donut queue with the following functions"""
    def __init__(self) -> None:
        self.normq: List[Any] = list()
        self.vipq: List[Any] = list()

    def arrive(self, name: str, vip: bool) -> None:
            """Adds the customer inside the queue"""
            if vip==True:
                self.vipq.append(name)
            else:
                self.normq.append(name)

    def next_customer(self) -> Optional[str]:
        """Fetches the next customer in proper order"""
        if len(self.normq)==0 and len(self.vipq)==0:
            return None
        if not len(self.vipq)==0:
            return self.vipq.pop(0)
        if not len(self.normq) == 0:
            return self.normq.pop(0)

    def waiting(self) -> Optional[str]:
        """ Prints all the names of cutomer in waiting queue in proper order"""
        if len(self.normq) == 0 and len(self.vipq) == 0:
            return None
        return ", ".join(self.vipq + self.normq)



# a=HW06.list_copy([1,2,3])
# b=HW06.list_intersect([], [])
# c=HW06.list_difference([1, 2, 3,7,8,9], [4, 5, 6])
# d=HW06.remove_vowels("Jan is my best friend")
# e=HW06.check_pwd("ABcC1")
# dq = DonutQueue()
# dq.arrive("Sujit", False)
# dq.arrive("Fei", False)
# dq.arrive("Prof JR", False)
# print(dq.waiting())
# dq.arrive("Nanda", False)
# print(dq.waiting())
# # print(dq.next_customer())
# # print(dq.next_customer())
# # print(dq.next_customer())
# # print(dq.next_customer())
# # print(dq.next_customer())
# z=HW06.reorder([1, 5, 3, 3, 7])
# print(z)