Sum = 0
Answer = []

for I in range(3):
    for J in range(int(input())):
        Sum += int(input())
    Answer.append("-" if Sum < 0 else "+" if Sum > 0 else "0")
    Sum = 0

print("\n".join(Answer))
