import Queue
import sys

Q = Queue.Basic()
Input = []

while True:
    Input.extend(list(sys.stdin.readline().rstrip().split()))

    if Input[0] == "empty":
        print(Q.IsEmpty())
    elif Input[0] == "size":
        print(Q.Size())
    elif Input[0] == "front":
        print(Q.Front())
    elif Input[0] == "back":
        print(Q.Back())
    elif Input[0] == "pop":
        print(Q.Pop())
    else:
        print(Q.Push(int(Input[1])))

    Input.clear()
