# Given the head of a singly linked list, return true if it is a 
# palindrome
#  or false otherwise.
# Example 1:
# Input: head = [1,2,2,1]
# Output: true
# Example 2:
# Input: head = [1,2]
# Output: false

class Solution:
    def reverse(self, head: ListNode) -> ListNode: # type: ignore
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool: # type: ignore
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = self.reverse(slow)
        while rev:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
        return True
    
# link  to solution approach:
# https://leetcode.com/problems/palindrome-linked-list/solutions/4908031/interview-approach-4-approach-list-stack-recursion-two-pointer-approach