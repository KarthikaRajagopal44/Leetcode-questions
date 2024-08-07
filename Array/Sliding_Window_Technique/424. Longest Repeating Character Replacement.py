# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.
# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        max_length = 0
        max_freq = 0
        left = 0

        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            max_freq = max(max_freq, char_count[s[right]])

            if (right - left + 1) - max_freq > k:
                char_count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length       
    
# link  to solution approach:
# https://leetcode.com/problems/longest-repeating-character-replacement/solutions/5584196/beats-93-59-easy-video-dry-run-flow-chart-line-by-line-explanation-beginner-friendly