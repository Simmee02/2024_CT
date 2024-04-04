M = int(input())
N = int(input())

is_prime = [True] * (N+1)
is_prime[0]=is_prime[1]= False
result =[]
prime_sum = 0
minValue = 0

p=2
while (p*p<=N):
    if (is_prime[p]==True):
        for i in range(p*p,N+1,p):
            is_prime[i] = False
    p+=1

for i in range(M,N+1):
    if is_prime[i]:
        result.append(i)


if (len(result)==0):
    print("-1")
else:
    for i in range(len(result)):
        prime_sum = prime_sum+result[i]
    result.sort()
    print(prime_sum)
    print(result[0])