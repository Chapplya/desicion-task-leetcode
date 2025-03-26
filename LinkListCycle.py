class Solution:
    def hasCycle(self, head) -> bool:
        tmp1 = head
        tmp2 = head
        while tmp1 and tmp1.next:
            tmp2 = tmp2.next.next
            tmp1 = tmp1.next
        if tmp1 == tmp2:
            return True
        return False


# Тестил код прямо на ликоде, тк. писать циклический список в падлу :)
