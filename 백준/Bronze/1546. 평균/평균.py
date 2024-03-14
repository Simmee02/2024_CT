N= int(input())
result_list= list(map(int,input().split()))
best_score=0
total=0

result_list.sort()
best_score = max(result_list)

for i in result_list:
    total += i/best_score*100

result=total/N
print(result)