class Solution:
    def hasCycle(self, head) -> bool:
        tmp = head
        sets = set()
        while tmp and tmp.val not in sets:
            sets.add((tmp.val))
            tmp = tmp.next
        if not (tmp):
            return False
        return True


# Тестил код прямо на ликоде, тк. писать циклический список в падлу :)
