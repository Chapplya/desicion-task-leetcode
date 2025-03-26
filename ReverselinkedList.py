class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, root):
        self.root = root

    def add(self, val):
        tmp = self.root
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(val=val)

    def print_lst(self):
        tmp = self.root

        while tmp:
            print(tmp.val, end=" ")
            tmp = tmp.next

    def reverseList(self):
        tmp = self.root
        cur = None
        while tmp:
            nxt = tmp.next
            tmp.next = cur
            cur = tmp
            tmp = nxt
        self.root = cur


root = Node(10)

lst = Solution(root=root)

lst.add(5)
lst.print_lst()
lst.reverseList()
print(" ")
lst.print_lst()
