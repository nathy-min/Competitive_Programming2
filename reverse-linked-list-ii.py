# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head
		
        h1 = dummy = head
        
        i = 1
        part = newHead = ListNode(None)
        
        while dummy:
            if i >= left and i <= right:
                tmp = ListNode(dummy.val)
                newHead.next = tmp
                newHead = newHead.next
            i += 1
            
            dummy = dummy.next
        
        part_rv = None
        
        while part:
            nxt = part.next
            
            part.next = part_rv
            part_rv = part
            part = nxt
            
        i = 1
        dummy = head
        while dummy:
            if i >= left and i <= right:
                dummy.val = part_rv.val
                part_rv = part_rv.next
            i += 1
            dummy = dummy.next
        return head