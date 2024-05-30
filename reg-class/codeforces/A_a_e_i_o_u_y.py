vowels = {"a","e", "i","o","u","y"}

n = int(input())
word  = input()

stack = []

for c in word:
    if stack and stack[-1] in vowels and c in vowels:
            continue
    else:
        stack.append(c)

print("".join(stack))