list= [-1]*26
s= input()

for i in range(len(s)):
    char = s[i]
    index= ord(char)- ord('a')
    if list[index] == -1:
        list[index] = i

print(' '.join(map(str,list)))
