_max , cnt = 0, 0
for i in range(1,10):
    n = int(input())
    _max = max(_max, n)
    if _max == n:
      cnt = i
print(_max, cnt, sep='\n')