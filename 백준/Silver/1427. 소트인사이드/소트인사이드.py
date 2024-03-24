numbers = list(map(int,list(input())))
numbers.sort()
numbers.reverse()

print(''.join(map(str,numbers)))