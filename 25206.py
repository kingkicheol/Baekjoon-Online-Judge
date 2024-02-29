x = 0
score = 0
score_dict = {'A+': 4.5, 'A0': 4, 'B+': 3.5, 'B0': 3, 'C+': 2.5, 'C0': 2, 'D+': 1.5, 'D0': 1, 'F': 0}
for i in range(20):
    n = input().split()
    if n[2] == 'P':
        continue
    x += float(n[1])
    score += score_dict[n[2]] * float(n[1])

print(score/x)