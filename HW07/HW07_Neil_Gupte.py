
"""Program to implement functions using python containers"""
from typing import *
from collections import defaultdict,Counter

class HW07:

    def anagrams_lst(str1: str, str2: str) -> bool:
        """finds if the two strings are anagrams of each other using list"""
        return sorted(list(str1.lower())) == sorted(list(str2.lower()))

    def anagrams_dd(str1: str, str2: str) -> bool:
        """finds if the two strings are anagrams of each other using dictionary"""
        dd:DefaultDict[str,int]=defaultdict(int)
        for i in str1.lower():
            dd[i]+=1
        for c in str2.lower():
            if c not in dd.keys():
                return False
            dd[c]-=1
        return not (any(dd.values()))

    def anagrams_cntr(str1: str, str2: str) -> bool:
        """finds if the two strings are anagrams of each other using Counter"""
        return Counter(str1.lower()) == Counter(str2.lower())


    def covers_alphabet(sentence: str) -> bool:
        """finds if the given string has all alphabet chars at least once"""
        return set(sentence.lower()) >= set('abcdefghijklmnopqrstuvwxyz')

    def web_analyzer(weblogs: List[Tuple[str, str]]) -> List[Tuple[str, List[str]]]:

        """function which accepts list of websites and employees and return sorted List of Tuples where Tuple[0] =site and
        Tuple[1] is list of employees"""

        dd: DefaultDict[str, str] = defaultdict(set)

        for item in weblogs:
            dd[item[1]].add(item[0])
        final:List=[ (site, sorted(list(dd[site]))) for site in dd]
        return sorted(final)











# print(HW07.anagrams_lst("12A","12a"))
# print(HW07.anagrams_dd("abcd","aabbccdd"))
# print(HW07.anagrams_cntr("abcde  ","abcde  "))
#print(HW07.covers_alphabet("bAbCdefghiJklomnopqrStuvwxy1z2222"))
# print(HW07.web_analyzer([('Nanda', 'google.com'), ('Maha', 'google.com'),
#  ('Fei', 'python.org'), ('Maha', 'google.com'),('Amir', 'apple.com'),('Zeeshan', 'zumba.com')]))