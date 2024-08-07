# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.
# Example 1:

# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:        
        stck = []    
        
        for c in s:                            
            if stck and stck[-1][0] == c: # check if stack is not empty
                stck[-1][1]+=1
                if stck[-1][1] == k:
                    stck.pop()
            else:
                stck.append([c, 1])            
        
        return ''.join(c * cnt for c, cnt in stck)            
    
    # https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/solutions/2012318/python-simple-one-pass-solution