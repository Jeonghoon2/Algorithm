class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pt = dummy.next
        prev_node = dummy
        
        while pt and pt.next:  
            current_node = pt
            next_node = current_node.next
            
            current_node.next = next_node.next
            next_node.next = current_node
            prev_node.next = next_node
            prev_node = current_node
            
            pt = current_node.next
            
        return dummy.next