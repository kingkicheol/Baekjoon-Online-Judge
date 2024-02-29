real_max_value = -1
real_max_value_row = 0
real_max_value_col = 0
for i in range(1, 10):
    row = list(map(int, input().split()))
    max_value = max(row)
    if max_value > real_max_value:
        real_max_value = max_value
        real_max_value_row = i
        real_max_value_col = row.index(real_max_value) + 1
print(real_max_value)
print(real_max_value_row, real_max_value_col)