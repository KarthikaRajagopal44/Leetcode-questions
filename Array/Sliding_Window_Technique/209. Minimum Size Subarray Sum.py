# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, curr_sum = 0,0,nums[0]
        res = float('inf')

        while True:
            if curr_sum >= target:
                res = min(res, r-l+1)
                curr_sum -= nums[l]
                l += 1
            else:
                r += 1
                if r >= len(nums):
                    break
                curr_sum += nums[r]
        
        return res if res != float('inf') else 0
    
# link  to solution approach:
    # https://leetcode.com/problems/minimum-size-subarray-sum/solutions/5348515/python-sliding-window-and-binary-search-solutions