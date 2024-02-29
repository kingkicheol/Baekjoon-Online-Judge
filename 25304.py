X = int(input())
Y = int(input())
for i in range(Y):
    a, b = map(int, input().split())
    X -= a*b
if X == 0:
    print('Yes')
else:
    print('No')