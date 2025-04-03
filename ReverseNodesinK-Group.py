
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k: int) -> :
        result = ListNode(0, head)
        temp = result

        while True:
            tmp = self.lenn(temp, k)
            if not tmp:
                break

            next_gr = tmp.next

            prev = tmp.next
            first = temp.next

            while first != next_gr:
                nxt = first.next
                first.next = prev
                prev = first
                first = nxt

            nxt = temp.next
            temp.next = tmp

            temp = nxt

        return result.next

    def lenn(self, head, k):
        while head and k > 0:
            k -= 1
            head = head.next
        return head
