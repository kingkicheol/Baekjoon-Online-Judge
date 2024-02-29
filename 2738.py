n, m = map(int, input().split())
a, b = [], []

for _ in range(n):
    a.append(list(map(int, input().split())))

for _ in range(n):
    b.append(list(map(int, input().split())))

for i, j in zip(a, b):
    c = []
    for k, l in zip(i, j):
        c.append(str(k + l))
    print(' '.join(c))