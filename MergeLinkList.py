class Solution:
    def reorderList(self, head) -> None:
        if not head or not head.next:
            return
 
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        second_half = slow.next
        slow.next = None 
        prev = None
        

        while second_half:
            nxt = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = nxt
        

        first_half = head
        second_half = prev
        
        while second_half:
            temp1 = first_half.next
            temp2 = second_half.next
            
            first_half.next = second_half
            second_half.next = temp1
            
            first_half = temp1
            second_half = temp2

