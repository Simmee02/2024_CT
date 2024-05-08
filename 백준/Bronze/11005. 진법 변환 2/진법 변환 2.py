def convert_to_base(n, b):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        remainder = n % b
        if remainder >= 10:
            digits.append(chr(remainder - 10 + ord('A')))
        else:
            digits.append(str(remainder))
        n = n // b
    digits.reverse()
    return ''.join(digits)


N, B = map(int, input().split())
result = convert_to_base(N, B)
print(result)
