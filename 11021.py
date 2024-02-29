n = int(input())+1
for i in range(1, n):
    a, b = map(int, input().split())
    print(f"Case #{i}: {a+b}")