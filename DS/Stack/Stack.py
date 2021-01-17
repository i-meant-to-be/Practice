class Stack:
    Arr = []

    def IsEmpty(self):
        return True if len(self.Arr) == 0 else False

    def Pop(self):
        return self.Arr.pop() if self.IsEmpty() is False else None

    def Push(self, Input):
        self.Arr.append(Input)

    def Peek(self):
        return self.Arr[-1] if self.IsEmpty() is False else None

    def HowMany(self):
        return len(self.Arr)


if __name__ == '__main__':
    stack = Stack()
    stack.Push(3)
    stack.Push(4)
    print(stack.Pop())
    print(stack.Peek())
    print(stack.HowMany())
    print(stack.IsEmpty())
    print(stack.Pop())
    print(stack.IsEmpty())
