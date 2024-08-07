# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.


# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix_sum = 0
        prefix_sum_count = {0: 1}  # Initialize with prefix sum 0 and count 1
        
        for num in nums:
            prefix_sum += num  # Update the running prefix sum
            if (prefix_sum - k) in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - k]  # Increment count if (prefix_sum - k) is found
            if prefix_sum in prefix_sum_count:
                prefix_sum_count[prefix_sum] += 1  # Update the frequency of the current prefix sum
            else:
                prefix_sum_count[prefix_sum] = 1  # Initialize the frequency if the prefix sum is seen for the first time
        
        return count
    
    # https://leetcode.com/problems/subarray-sum-equals-k/solutions/5334031/python-100-beat-100-efficient-optimal-solution-easy-to-understand