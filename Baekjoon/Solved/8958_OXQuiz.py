from sys import stdin

input = stdin.readline
num = int(input())
for _ in range(num):
    answer = input()
    counter = 0
    score = 0
    for i in range(len(answer) - 1):
        if answer[i] == 'O':
            counter += 1
            score += counter
        else:
            counter = 0
    print(score)
