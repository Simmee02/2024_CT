s=input().upper()
frequency = {}
max_count = 0
max_char = ''

for char in s:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

for char,count in frequency.items():
    if count > max_count:
        max_count = count
        max_char = char
    elif count == max_count:
        max_char='?'

print(max_char)