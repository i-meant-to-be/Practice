from sys import stdin

input = stdin.readline

h, m, s = [int(num) for num in input().rstrip().split()]
cookingTime = int(input().rstrip())

cookingS = cookingTime % 60
tempMin = cookingTime // 60
cookingM = tempMin % 60
cookingH = tempMin // 60

if s + cookingS >= 60:
    cookingS -= 60
    m += 1
s += cookingS

if m + cookingM >= 60:
    cookingM -= 60
    h += 1
m += cookingM

h = (h + cookingH) % 24

print(f"{h} {m} {s}")
