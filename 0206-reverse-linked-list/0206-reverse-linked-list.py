# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,node1, node2):
        if not node2:
            return
        temp = node2.next
        node2.next = node1
        self.reverse(node2, temp)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        
        while temp and temp.next:
            temp = temp.next
        
        self.reverse(None, head)
        return temp