# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# Example 1:
#
#
# Input: 1->1->2
# Output: 1->2
#
#
# Example 2:
#
#
# Input: 1->1->2->3->3
# Output: 1->2->3
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        p = head
        
        if not p or not p.next: return head
        
        while p.next:
            
            if p.val == p.next.val:
                if p.next.next:
                    p.next = p.next.next
                else:
                    p.next = None
            else:
                p = p.next
                    
        return head
                    
                
                
