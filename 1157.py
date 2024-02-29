st = input().upper()
st_list = list(set(st))
count = []
for i in st_list:
  count.append(st.count(i))
print(st_list[count.index(max(count))] if count.count(max(count)) == 1 else '?')