# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

 

# Example 1:

# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
# Example 2:

# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].

from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int) # defaultdict to store the frequency of the elements in the subarray
        i, j = 0, 0 # variables i and j are used to keep track of the subarray boundaries
        for j in range(len(fruits)):
            count[fruits[j]] += 1 # increase the count of the current fruit
            if len(count) > 2: 
                count[fruits[i]] -= 1 # reduce the count of the first fruit
                if count[fruits[i]] == 0:
                    del count[fruits[i]] # remove the first fruit from the defaultdict if its count becomes 0
                i += 1 # move the start of the subarray to the right
        return j - i + 1 # return the length of the longest subarray with at most two unique elements
    
    # https://leetcode.com/problems/fruit-into-baskets/solutions/3153579/super-easy-solution-fully-explained-c-python-commented