
arr1 = input()
arr2 = input()

path = [[0] * (len(arr2) + 1) for _ in range(len(arr1) + 1)]

for i in range(len(arr1) -1, -1, -1):
    for j in range(len(arr2) -1, -1, -1):

        if arr1[i] == arr2[j]:
            path[i][j] = 1 + path[i + 1][j + 1]
        else:
            if path[i + 1][j] > path[i][j + 1]:
                path[i][j] = path[i + 1][j]
            else:
                path[i][j] = path[i][j + 1]

ans = [] 
i = j = 0             
while i < len(arr1) and j < len(arr2):
    if arr1[i] == arr2[j]:
        ans.append(arr1[i])
        i += 1
        j += 1
    else:
        if path[i + 1][j] > path[i][j + 1]:
            i += 1
        else:
            j += 1

print("".join(ans))





