# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        node = ListNode()
        node.next = head.next
        temp = head.next.next
        head.next.next = head
        head.next = self.swapPairs(temp)
        return node.next