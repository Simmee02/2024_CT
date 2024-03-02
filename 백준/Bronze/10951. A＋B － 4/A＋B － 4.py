while True:
    try:
        input_str = input()
        if not input_str:
            break
        a, b = map(int, input_str.split())
        print(a + b)
    except EOFError:  # 입력의 끝에 도달했을 때
        break