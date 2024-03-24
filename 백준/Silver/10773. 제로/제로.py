k = int(input())
numbers = []
sum =0

for i in range(k):
    a = int(input())
    if a != 0:
        numbers.append(a)
    else:
        numbers.pop()

for j in range(len(numbers)):
    sum=sum+numbers[j]

print(sum)