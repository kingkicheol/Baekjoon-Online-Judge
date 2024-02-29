N = int(input())
n = 2*N-1
for i in range(1, n+1):
    print(' '*abs(N-i)+'*'*(n-(2*abs(N-i))))