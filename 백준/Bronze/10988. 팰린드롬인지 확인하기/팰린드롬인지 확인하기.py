s=input()
s_reverse=''.join(reversed(s))

if s == s_reverse:
    print(1)
else:
    print(0)