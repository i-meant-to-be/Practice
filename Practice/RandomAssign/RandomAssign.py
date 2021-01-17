import random

''' 인원 수 설정 '''
Num = list(range(10))

''' 파일 불러오기 '''
try:
    FArea = open("Area.txt")
    FPrev = open("Prev.txt")

except FileNotFoundError:
    print("파일을 찾을 수 없음.")
    exit()

''' 데이터 불러오기 '''
Prev = [list(map(int, (Set.split(" ")))) for Set in FPrev.read().split("\n")]
Set = zip(Num, Prev)
Area = FArea.read().split("\n")

''' 구역 배정 '''
for I in range(len(Num)):
    Temp = random
    if Set[1][0] == 
