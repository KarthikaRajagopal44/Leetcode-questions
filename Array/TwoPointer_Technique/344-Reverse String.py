# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# Example usage:
s1 = ["h", "e", "l", "l", "o"]
solution = Solution()
solution.reverseString(s1)  # Use the updated method name
print(s1)  # Output: ["o", "l", "l", "e", "h"]


# link  to solution approach:
# https://leetcode.com/problems/reverse-string/solutions/5242849/faster-less-mem-2-methods-detailed-approach-2-ptr-recursion-python-java-c