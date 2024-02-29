T = int(input())
for i in range(T):
    R, S = input().split()
    total = ''
    for j in S:
        total += j * int(R)
    print(total)