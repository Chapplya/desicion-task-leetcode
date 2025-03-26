
class Solution:
    def __init__(self, root1, root2, res):
        self.root1 = root1
        self.root2 = root2
        self.res = res
        
    def mergeTwoLists(self):
        lst1 = self.root1
        lst2 = self.root2
        start_res = self.res
        new_lst = start_res

        while lst1 and lst2:
            if lst1.val > lst2.val:
                new_lst.next = lst2
                lst2 = lst2.next
            else:
                new_lst.next = lst1
                lst1 = lst1.next
            new_lst = new_lst.next
        new_lst.next = lst1 or lst2

        self.res = start_res.next

