class MinStack:
    def __init__(self):
        self.stack = []
        self.list_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.list_min:
            self.list_min.append(val)
        else:
            if self.list_min[-1] >= val:
                self.list_min.append(val)

    def pop(self) -> None:
        del_el = self.stack.pop()
        if del_el == self.list_min[-1]:
            self.list_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.list_min[-1]


stack = [1, 2]
minn = [1, 1]


minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
