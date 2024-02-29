h, m = map(int, input().split())
t = int(input())
m += t
if m < 60:
    print(h, m)
else:
    h = h + (m // 60)
    m = m % 60
    if h > 23:
        print(h-24, m)
    else:
        print(h, m)