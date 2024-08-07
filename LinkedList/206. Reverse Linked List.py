# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        node = None

        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp
        
        return node
    
    # https://leetcode.com/problems/reverse-linked-list/solutions/5152548/video-solution-with-visualization