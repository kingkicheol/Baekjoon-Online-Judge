N, M = map(int, input().split())
basket = [n+1 for n in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    n1, n2 = basket[i-1], basket[j-1] 
    basket[i-1], basket[j-1] = n2, n1
print(' '.join(map(str, basket)))