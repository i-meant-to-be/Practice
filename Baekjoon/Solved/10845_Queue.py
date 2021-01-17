import sys

A = []
Com = []
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    Com = list(sys.stdin.readline().rstrip().split())

    if Com[0] == "empty":
        print(1 if len(A) == 0 else 0)
    elif Com[0] == "size":
        print(len(A))
    elif Com[0] == "front":
        print(A[0] if len(A) != 0 else -1)
    elif Com[0] == "back":
        print(A[len(A) - 1] if len(A) != 0 else -1)
    elif Com[0] == "pop":
        print(A.pop(0) if len(A) != 0 else -1)
    else:
        A.append(int(Com[1]))
