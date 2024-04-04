N = int(input())
temp = 2
dot = 0
for i in range(N):
    dot = (temp+(2**(i+1-1)))**2
    temp = temp+(2**(i+1-1))

print(dot)