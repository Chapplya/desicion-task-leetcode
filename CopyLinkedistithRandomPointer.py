"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        # 1. Создаем копии узлов и сохраняем соответствие оригинал:копия в словаре
        node_map = {}
        curr = head
        while curr:
            node_map[curr] = Node(curr.val)

            curr = curr.next

        curr = head
        while curr:
            copy_node = node_map[curr]
            copy_node.next = node_map.get(
                curr.next
            )  # get() возвращает None, если ключа нет
            copy_node.random = node_map.get(curr.random)
            curr = curr.next

        return node_map[head]
