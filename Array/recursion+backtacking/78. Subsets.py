# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # This list will store all the subsets
        res = []
        # This list will store the current subset being built
        subset = []

        # Helper function to recursively build subsets
        def create_subset(i):
            # Base case: if we have considered all elements
            if i == len(nums):
                # Add a copy of the current subset to the result list
                res.append(subset[:])
                return
            
            # Include the current element in the subset
            subset.append(nums[i])
            # Recursively build subsets including the current element
            create_subset(i + 1)

            # Exclude the current element from the subset (backtrack)
            subset.pop()
            # Recursively build subsets excluding the current element
            create_subset(i + 1)

        # Start the recursion with the first index
        create_subset(0)
        # Return all the subsets collected
        return res
