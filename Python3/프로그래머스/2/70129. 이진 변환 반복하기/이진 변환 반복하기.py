# def solution(s):
#     count_one = s.count("1")
#     one = int("1" * count_one)  
#     zero = len(s) - count_one

#     result = []
#     count = 0

#     while True:
#         if one == 1:
#             break

#         result.append(one % 2)
#         one = one // 2
#         count += 1

#     answer = [count, zero]

#     return answer

def solution(s):
    count = 0
    zero = 0

    while s != "1":
        zero += s.count("0")

        length = len(s) - s.count("0")
        s = bin(length)[2:] #0b110 형태 -> 슬라이싱으로 0b 제거

        count += 1

    return [count, zero]