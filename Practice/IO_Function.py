def Sum(A, B):
    return A + B


def SumPrint(A, B):
    print("%d, %d의 합은 %d입니다." % (A, B, A + B))


"""
print(Sum(3, 4))
SumPrint(3, 4)
"""

# input
A = int(input("첫 번째 숫자 입력: "))
B = int(input("두 번째 숫자 입력: "))

print(Sum(A, B))
SumPrint(A, B)

# input + split
A, B = input("자연수 두 개 입력: ").split()
A = int(A)
B = int(B)

print(Sum(A, B))
SumPrint(A, B)

# input + split + map
A, B = list(map(int, input("자연수 두 개 입력: ").split()))

print(Sum(A, B))
SumPrint(A, B)
