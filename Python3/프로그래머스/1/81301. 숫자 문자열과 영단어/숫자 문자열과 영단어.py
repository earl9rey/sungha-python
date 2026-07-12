def solution(s):
    d = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    
    idx = 0
    answer = []
    
    while idx < len(s):
        if s[idx].isdigit():
            answer.append(s[idx])
            idx += 1

        else:        
            word = ""
            while word not in d:
                word += s[idx] # 한 글자씩 단어 만들기
                idx += 1
            answer.append(str(d[word]))

    return int("".join(answer))
            

    return answer


# def solution(s):
#     words = {
#         "zero": "0",
#         "one": "1",
#         "two": "2",
#         "three": "3",
#         "four": "4",
#         "five": "5",
#         "six": "6",
#         "seven": "7",
#         "eight": "8",
#         "nine": "9"
#     }

#     for word, num in words.items():
#         s = s.replace(word, num)

#     return int(s)