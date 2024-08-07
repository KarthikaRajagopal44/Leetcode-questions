from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found
    
    # https://leetcode.com/problems/two-sum/solutions/3619262/3-method-s-c-java-python-beginner-friendly