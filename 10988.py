palindrome = list(input())
palindrome_len = len(palindrome)//2
count = 0
for i in range(1, palindrome_len + 1):
    if palindrome.pop(0) != palindrome.pop():
        break
    count = i
print(1 if palindrome_len == count else 0)