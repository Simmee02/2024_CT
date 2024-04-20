def solution(numbers):
    sum = 45
    temps = []
    for i in range(10):
        temps.append(i)
    for i in range(len(numbers)):
        if numbers[i] in temps:
            sum = sum - numbers[i]
    return sum
        