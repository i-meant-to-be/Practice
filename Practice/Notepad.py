from sys import stdin

input = stdin.readline
pixels = list()
new_pixels = list()
N, K = [int(num) for num in input().split()]
for _ in range(N):
    pixels.append(input().split())
print(pixels)
for i in range(N):
    for j in range(len(pixels[i])):
        pixels[i][j] = pixels[i][j] * K
for i in range(N):
    for _ in range(K):
        new_pixels.append(pixels[i])
for i in range)
print(new_pixels)

