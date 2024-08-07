# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1
        
        return res
# Example usage
nums1 = [-4, -1, 0, 3, 10]
nums2 = [-7, -3, 2, 3, 11]

sol = Solution()
print(sol.sortedSquares(nums1))  # Output: [0, 1, 9, 16, 100]
print(sol.sortedSquares(nums2))  # Output: [4, 9, 9, 49, 121]

# link  to solution approach:
# https://leetcode.com/problems/squares-of-a-sorted-array/solutions/5418442/video-using-two-pointers