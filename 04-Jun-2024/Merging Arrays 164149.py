# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n,m = list(map(int,input().split()))
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

l,r = 0,0
arr = []
while l< len(arr1) and r<len(arr2):

    if arr1[l] <= arr2[r]:
        arr.append(arr1[l])

        l+=1
    else:
        arr.append(arr2[r])
        r+=1
    

arr.extend(arr1[l:])
arr.extend(arr2[r:])


for ar in arr:
    print(ar,end=" ")