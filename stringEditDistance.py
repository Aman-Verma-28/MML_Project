from sys import stdin, stdout
from collections import Counter, deque
from math import *
# from functools import reduce
from bisect import bisect_right
from heapq import *
# from itertools import permutations
cin = stdin.readline
cout = stdout.write
mod = 1000000007


# ----------     PROBLEM STATEMENT    ----------- #
problemStatement = '''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
-------  XXXXXX -------------
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

'''


def inpn():
    return int(cin())


def inpl():
    return list(map(int, cin().split()))


def inpset():
    return set(map(int, cin().split()))


def inps():
    return cin()[:-1]


def inpv():
    return map(int, cin().split())


def inpvf():
    return map(float, cin().split())


def outs(s):
    cout(s)


def outn(n):
    cout(str(n))


def outl(l):
    for i in l:
        cout(str(i) + " ")


def outb(s):
    cout(str(s))


def endl():
    cout("\n")


def helperForMemotization(
    word1: str,
    word2: str,
    first: int,
    second: int,
    memo: dict = dict(),
):
    len1 = len(word1)
    len2 = len(word2)

    if (first, second) in memo:
        return memo[(first, second)]

    elif first >= len1 and second >= len2:
        return 0

    elif first >= len1 or second >= len2:
        if first >= len1:
            return len2 - second
        else:
            return len1 - first

    else:
        if word1[first] == word2[second]:
            return helperForMemotization(word1, word2, first+1, second+1, memo)

        else:
            possibility1 = 1 + helperForMemotization(word1, word2, first+1, second+1, memo)
            possibility2 = 1 + helperForMemotization(word1, word2, first+1, second, memo)
            possibility3 = 1 + helperForMemotization(word1, word2, first, second+1, memo)

            memo[(first, second)] = min(possibility1, possibility2, possibility3)

            return memo[(first, second)]


def recursiveAndMemoizationApproach(
        word1: str,
        word2: str,
) -> int:

    return helperForMemotization(
        word1=word1,
        word2=word2,
        first=0,
        second=0,
    )


if __name__ == '__main__':
    outs("Enter the first word: ")
    word1 = inps()
    outs("Enter the second word: ")
    word2 = inps()

    stringEditDistance = recursiveAndMemoizationApproach(
        word1=word1,
        word2=word2,
    )

    outs("The string edit distance is between word1 = {} and word2 = {}: ".format(word1, word2))
    outn(stringEditDistance)
    endl()


