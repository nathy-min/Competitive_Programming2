# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def divide(self, head):
        if not head:
            return head
        if not head.next:
            return self.merge(head , [])
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        temp = slow.next
        slow.next = None 
        
        conq1 = self.divide(head)
        conq2 = self.divide(temp)
        # print(head
        return self.merge(conq1, conq2)
    
    def merge(self, head1, head2):
        if not head2:
            return head1
        node = ListNode(0)
        temp = node
        
        while head1 and head2:
            if head1.val <= head2.val:
                temp.next = head1
                head1 = head1.next
                temp = temp.next
            else:
                temp.next = head2
                head2 = head2.next
                temp = temp.next
        
        if head1:
            temp.next = head1
        elif head2:
            temp.next = head2 
    
        return node.next    
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.divide(head)
        