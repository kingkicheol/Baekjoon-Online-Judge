remain = []
for _ in range(10):
    a = int(input()) % 42
    if a not in remain:
        remain.append(a)
print(len(remain))