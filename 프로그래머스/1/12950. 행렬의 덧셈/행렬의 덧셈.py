def solution(arr1, arr2):
    ans =[]
    for i in range(len(arr1)):
        row =[]
        for j in range(len(arr1[0])):
            row.append(arr1[i][j]+arr2[i][j])
        ans.append(row)
    
    return ans