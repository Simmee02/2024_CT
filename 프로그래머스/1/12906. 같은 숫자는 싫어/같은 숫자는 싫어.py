def solution(arr):
    ans = []
    for i in range(len(arr)):
        if i == 0:
            ans.append(arr[i])
        else:
            if arr[i] != arr[i-1]:
                ans.append(arr[i])
    return ans