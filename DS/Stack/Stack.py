class Basic:
    Arr = []
    Top = -1

    def Pop(self):
        if self.IsEmpty() is True:
            print(" - 오류 발생: 스택이 비어 있음\n")
        else:
            Temp = self.Arr[self.Top]
            del self.Arr[self.Top]
            self.Top -= 1
            return Temp

    def Push(self, Input):
        self.Arr.append(Input)
        self.Top += 1
        return Input

    def IsEmpty(self):
        if self.Top is -1:
            return True
        else:
            return False

    def Peek(self):
        if self.IsEmpty() is True:
            print(" - 오류 발생: 스택이 비어 있음\n")
        else:
            return self.Arr[self.Top]

    def HowMany(self):
        return self.Top + 1


class BOJ(Basic):

    def Pop(self):
        if self.IsEmpty() is True:
            return -1
        else:
            Temp = self.Arr[self.Top]
            del self.Arr[self.Top]
            self.Top -= 1
            return Temp

    def Peek(self):
        if self.IsEmpty() is True:
            return -1
        else:
            return self.Arr[self.Top]
