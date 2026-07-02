from collections import deque

def solution(food):
    dq = deque()
    dq.append("0")

    for i in range(len(food) - 1, 0, -1):
        dq.appendleft(str(i) * (food[i] // 2))
        dq.append(str(i) * (food[i] // 2))

    answer = "".join(dq)
    return answer

# def solution(food):
#     left = []

#     for i in range(1, len(food)):
#         left.append(str(i) * (food[i] // 2))

#     return "".join(left) + "0" + "".join(left[::-1])