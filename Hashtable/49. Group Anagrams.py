from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
    

    # https://leetcode.com/problems/group-anagrams/solutions/3687735/beats-100-c-java-python-beginner-friendly