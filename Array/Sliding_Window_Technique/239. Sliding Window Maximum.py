# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.
# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        output = []

        for idx, n in enumerate(nums):
            # getting rid of the idx that are outdated for our new window 
            while q and q[0] < idx - k + 1:
                q.popleft()
            
            # popping out numbers that are smaller than n from the right of the q 
            while q and n > nums[q[-1]]:
                q.pop()

            q.append(idx)

            # start logging answers after you have reached the desired window size of 'k'
            if idx >= k-1:
                output.append(nums[q[0]])

        return output 
    

    
    # https://leetcode.com/problems/sliding-window-maximum/solutions/4531425/python-easy-explanation-mind-map-diagram-fixed-size-sliding-window-algorithm-space-o-k