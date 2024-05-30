
n, k = map(int, input().split())
arr = list(map(int, input().split()))

suffix = [(0, -float('inf'))] * (n + 1)
for i in range(n - 1, -1 , -1):
    suffix[i] = (arr[i] + suffix[i + 1][0], i)

suffix.sort(reverse = True)

print(suffix)
pref = [0] * n
pref[0] = arr[0]

for i in range(1, n):
    pref[i] = arr[i] + pref[i - 1]



    
