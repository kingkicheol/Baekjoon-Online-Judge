tel = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
call = 0
for str in input():
    for i, t in enumerate(tel):
        if str in t:
            call += i+3
print(call)