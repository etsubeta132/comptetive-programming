# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n,m = list(map(int,input().split()))
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

res = []
ctr = 0
l = 0

for i in range(len(arr2)):
    
    while l < len(arr1) and arr1[l] < arr2[i]:
        ctr+=1
        l+=1
    
    res.append(ctr)

for ctr in res:
    print(ctr,end=" ")