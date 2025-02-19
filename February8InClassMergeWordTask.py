""" You are given two strings word1 and word2. Merge the strings by adding letters
in alternating order, starting with word1. If a string is longer than the other, append
the additional letters onto the end of the merged string."""


class Solution:
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2
        length1 = len(word1)
        length2 = len(word2)
        len1 = 0
        len2 = 0
        box = []
        """
                :type word1: str
                :type word2: str
                :rtype: str
     
               """
        word = 1
        while len1<length1 and len2<length2:
            if word == 1

     """  def merge_alternately(self):
        result = ""
        if len1 > len2:
            for i in range(len1):
                result += self.word1[i]
                result += self.word2[i]
            print(result, result[len2: len1])

        elif len2 > len1:
            result = ""
            for i in range(len2):
                result += self.word2[i]
                result += self.word1
            print(result, result[len1: len2])


first_word = input("What is your first word: ")
second_word = input("What is your second word: ")
mySolution = Solution(first_word, second_word)
mySolution.merge_alternately()
"""