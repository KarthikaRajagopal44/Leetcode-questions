# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        l = [0] * 26
        k = [0] * 26
        for c in p:
            k[ord(c) - ord('a')] += 1
        i = j = 0
        res = []
        while j < n:
            c = ord(s[j]) - ord('a')
            l[c] += 1
            if j - i + 1 < m:
                j += 1
            else:
                if l == k:
                    res.append(i)
                x = ord(s[i]) - ord('a')
                l[x] -= 1
                i += 1
                j += 1
        return res
    

    
    # https://leetcode.com/problems/find-all-anagrams-in-a-string/solutions/3146464/one-arrow-two-targets-ez-sliding-window-1-permutation-in-string-2-find-all-anagrams-in-a-string