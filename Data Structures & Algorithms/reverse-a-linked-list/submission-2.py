class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, curr = None, head

        while curr:
            # reversed the node
            temp = curr.next
            curr.next = prev
            
            # move to next iteration
            prev = curr
            curr = temp
        
        return prev
            