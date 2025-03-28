class Solution:
    def removeNthFromEnd(self, head, n: int):
        main = head
        length = 0
        while main:
            length += 1
            main = main.next
        cur = length - n
        count = 0
        main = head
        if cur == count:
            return head.next

        while count < cur - 1:
            main = main.next
            count += 1

        main.next = main.next.next

        return head
