
while True:
    temp = 0
    others = 0
    summ = 0
    nums = []
    nums=list(map(int,input().split()))
    summ = nums[0]+nums[1]+nums[2]
    if summ == 0:
        break
    for i in range(3):
        if temp <= nums[i]:
            temp = nums[i]
    others = summ-temp

    if temp<others:
        if nums[0]==nums[1]==nums[2]:
            print("Equilateral")
        elif nums[0]==nums[1] or nums[2]==nums[1] or nums[2]==nums[0]:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")




