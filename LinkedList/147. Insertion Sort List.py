# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

# The steps of the insertion sort algorithm:

# Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
# It repeats until no input elements remain.
# The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

# Example 1:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode: # type: ignore
        
        # No need to sort for empty list or list of size 1
        if not head or not head.next:
            return head
        
        # Use dummy_head will help us to handle insertion before head easily
        dummy_head = ListNode(val=-5000, next=head) # type: ignore
        last_sorted = head # last node of the sorted part
        cur = head.next # cur is always the next node of last_sorted
        while cur:
            if cur.val >= last_sorted.val:
                last_sorted = last_sorted.next
            else:
                # Search for the position to insert
                prev = dummy_head
                while prev.next.val <= cur.val:
                    prev = prev.next
                    
                # Insert
                last_sorted.next = cur.next
                cur.next = prev.next
                prev.next = cur
                
            cur = last_sorted.next
            
        return dummy_head.next
    

# https://leetcode.com/problems/insertion-sort-list/solutions/1176552/python3-188ms-solution-explanation-with-visualization