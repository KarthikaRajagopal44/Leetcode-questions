# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Base case: If there's only one number, return it as the only permutation
        if len(nums) == 1:
            return [nums[:]]
        
        res = []  # This will store all permutations

        # Iterate over each element in the list
        for _ in range(len(nums)):
            # Remove the first element from the list and store it in 'n'
            n = nums.pop(0)
            
            # Recursively find all permutations of the remaining elements
            perms = self.permute(nums)
            
            # Add the removed element 'n' to each permutation found
            for p in perms:
                p.append(n)
            
            # Add all these new permutations to the result list
            res.extend(perms)
            
            # Restore the original list by adding the removed element back
            nums.append(n)
        
        # Return the list of all permutations
        return res
