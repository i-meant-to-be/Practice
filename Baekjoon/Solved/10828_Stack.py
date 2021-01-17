import sys

Arr = []
Input = []
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    Input = sys.stdin.readline().rstrip().split(" ")

    if Input[0] == "push":
        Arr.append(Input[1])

    elif Input[0] == "pop":
        if not Arr:
            print(-1)
        else:
            print(Arr[-1])
            Arr.pop()

    elif Input[0] == "size":
        print(len(Arr))

    elif Input[0] == "empty":
        if not Arr:
            print(1)
        else:
            print(0)

    elif Input[0] == "top":
        if not Arr:
            print(-1)
        else:
            print(Arr[-1])
