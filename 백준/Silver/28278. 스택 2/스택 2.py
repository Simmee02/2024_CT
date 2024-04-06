import sys

N = int(input())
stack = []

for _ in range(N):
    order = sys.stdin.readline().strip()  # strip()
    if order.startswith("1 "):
        _, b = order.split()
        stack.append(int(b))
    elif order == "2":
        if not stack:
            print("-1")
        else:
            print(stack.pop())
    elif order == "3":
        print(len(stack))
    elif order == "4":
        print("1" if not stack else "0")
    elif order == "5":
        print("-1" if not stack else stack[-1])
