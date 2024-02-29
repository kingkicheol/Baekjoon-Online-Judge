N, M = map(int, input().split())
basket = [n+1 for n in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    basket2 = reversed(basket[i-1: j])
    basket[i-1: j] = basket2
for n in range(N):
    print(basket[n], end=' ')