# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.
# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc
class Solution:
    def decodeString(self, s: str) -> str:
        # Initialize the stack and the current string
        stack = []
        curr_str = ""
        # Initialize the current number to 0
        curr_num = 0
        
        # Iterate through each character of the string
        for c in s:
            # If the character is a digit, update the current number
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            # If the character is an opening bracket, push the current number and current string onto the stack
            elif c == "[":
                stack.append(curr_num)
                stack.append(curr_str)
                # Reset the current number and current string
                curr_num = 0
                curr_str = ""
            # If the character is a closing bracket, repeat the popped characters and push the result back onto the stack
            elif c == "]":
                prev_str = stack.pop()
                prev_num = stack.pop()
                curr_str = prev_str + curr_str * prev_num
            # If the character is a letter, append it to the current string
            else:
                curr_str += c
        
        # Pop any remaining characters from the stack and concatenate them to the final result
        while stack:
            curr_str = stack.pop() + curr_str
        
        return curr_str
    
    # https://leetcode.com/problems/decode-string/solutions/3258413/394-solution-with-step-by-step-explanation