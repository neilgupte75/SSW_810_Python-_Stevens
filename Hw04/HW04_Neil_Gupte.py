"""Hw 04 this program has 5 functions offers practice iterating over lists, ranges, and strings using for and while loops as well as using a generator of random integers. """
from typing import *
import random

def count_vowels(s: str) -> int:
    """function to return the number of vowels in given string"""
    vow_list:str=['a','e','i','o','u']
    s:str=s.lower()
    cnt:int=0
    for i in s:
        if i in vow_list:
            cnt+=1
    return cnt


def last_occurrence(target: Any, sequence: Sequence[Any]) -> Optional[int]:
    """function to print the index of last occurence of target inside a sequence returns None if target not in sequence"""
    if target not in sequence:
        return None
    else:
        val:Any
        off:Any
        return max(off for off, val in enumerate(sequence) if val == target)


def my_enumerate(seq: Sequence[Any]) -> Iterator[Any]:
    """generator which mimics enumerate functioning"""
    for i in range(len(seq)):
        yield i,seq[i]


def random_integer_generator(minimum: int, maximum: int) -> Iterator[int]:
    """Generator which fetches infinite sequence of random number between given values"""
    while True:
        r:int = random.randint(minimum, maximum)  # return a random integer between 0 and 10 inclusive.
        yield r


def find_target(target: int, min_val: int, max_val: int, max_attempts: int) -> Optional[int]:
    """function to return no of passes before which target is found and if not found then print None"""
    if not min_val<=target<=max_val:
        raise ValueError("Minimum Value Cannot be less Than Maximum, aslo check the target value")
    if not max_attempts>0:
        raise ValueError("Max attempts should be greater than 0")
    cnt:int=0
    iter:Iterator[int]=random_integer_generator(min_val,max_val)
    for item in iter:
        cnt+=1
        if cnt<=max_attempts:
            if item==target:
                return cnt
        else:
            return None
