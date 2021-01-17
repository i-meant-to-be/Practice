class Basic:
    A = []

    def IsEmpty(self):
        return 1 if len(self.A) == 0 else 0

    def Size(self):
        return len(self.A)

    def Front(self):
        return self.A[0] if self.IsEmpty() == 0 else -1

    def Push(self, N):
        self.A.append(N)
        return N

    def Back(self):
        return self.A[len(self.A) - 1] if self.IsEmpty() == 0 else -1

    def Pop(self):
        return self.A.pop(0) if self.IsEmpty() == 0 else -1
