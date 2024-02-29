black = [1, 1, 2, 2, 2, 8]
white = list(map(int, input().split()))
for i, j in zip(black, white):
    print(i - j)