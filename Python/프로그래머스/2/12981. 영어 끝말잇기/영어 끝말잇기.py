def solution(n, words):
    used = set()

    for i, word in enumerate(words):
        
        # 1. 이미 사용한 단어
        if word in used:
            return [i % n + 1, i // n + 1]
        
        # 2. 끝말잇기 실패
        if i > 0 and words[i - 1][-1] != word[0]:
            return [i % n + 1, i // n + 1]
        
        used.add(word)

    return [0, 0]