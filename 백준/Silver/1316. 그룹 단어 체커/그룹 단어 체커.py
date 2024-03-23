def is_group_word(word):
    seen = set()
    prev_char = ''
    for char in word:
        if char in seen and char != prev_char:
            return False
        seen.add(char)
        prev_char = char
    return True

def count_group_words(N):
    group_word_count = 0
    for _ in range(N):
        word = input()
        if is_group_word(word):
            group_word_count += 1
    return group_word_count

N = int(input())
print(count_group_words(N))
