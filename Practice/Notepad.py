from sys import stdin

input = stdin.readline
num = int(input())
deque = list()
for _ in range(num):
    command = input().rstrip().split()
    if command[0] == "size":
        print(len(deque))
    elif command[0] == "empty":
        print(1 if not len(deque) else 0)
    elif command[0] == "front":
        print(deque[0] if len(deque) else -1)
    elif command[0] == "back":
        print(deque[-1] if len(deque) else -1)
    elif command[0] == "pop_front":
        print(deque.pop(0) if len(deque) else -1)
    elif command[0] == "pop_back":
        print(deque.pop() if len(deque) else -1)
    elif command[0] == "push_front":
        deque.insert(0, int(command[1]))
    else:
        deque.append(int(command[1]))
