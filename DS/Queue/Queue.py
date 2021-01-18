# Basic queue
class Queue:
    Arr = []

    def IsEmpty(self):
        return True if len(self.Arr) == 0 else False

    def Size(self):
        return len(self.Arr)

    def Push(self, N):
        self.Arr.append(N)

    def Front(self):
        return self.Arr[0] if self.IsEmpty() == 0 else None

    def Back(self):
        return self.Arr[-1] if self.IsEmpty() == 0 else None

    def Pop(self):
        return self.Arr.pop(0) if self.IsEmpty() == 0 else None


# Deque (Double-ended queue)
class Deque(Queue):
    # Basic Push and Pop can't be used on deque.
    def Push(self, N):
        raise AttributeError("'Deque' object has no attribute 'Push'")

    def Pop(self):
        raise AttributeError("'Deque' object has no attribute 'Push'")

    def Insert_Front(self, N):
        self.Arr.insert(0, N)

    def Insert_Rear(self, N):
        self.Arr.append(N)

    def Delete_Front(self):
        return self.Arr.pop(0) if self.IsEmpty() == 0 else None

    def Delete_Rear(self):
        return self.Arr.pop() if self.IsEmpty() == 0 else None

    # Front
    # Back
    # IsEmpty
    # Size


# Priority queue
class Priority_Queue(Queue):
    pass


if __name__ == "__main__":
    deque = Deque()
    print(deque.IsEmpty())
    deque.Insert_Front(1)
    deque.Insert_Rear(100)
    deque.Insert_Front(32)
    deque.Insert_Rear(4444)
    print(deque.Arr)
    deque.Delete_Rear()
    print(deque.Arr)
    deque.Delete_Front()
    print(deque.Arr)
    deque.Pop()
