class Node:
    def __init__(self, val=None, next=None):
        self.val = None
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        result = Node()
        tmp = result
        ost = 0
        while l1 or l2 or ost:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            value = val1 + val2 + ost
            ost = value // 10
            val = value % 10
            tmp.next = Node(val)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return result.next
