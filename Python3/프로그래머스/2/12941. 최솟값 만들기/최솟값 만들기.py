# from itertools import permutations

# def solution(A, B):
#     answer = float('inf')

#     for perm in permutations(B):
#         total = sum(a * b for a, b in zip(A, perm))
#         answer = min(answer, total)

#     return answer

def solution(A, B):
    A.sort()
    B.sort(reverse=True)

    return sum(a * b for a, b in zip(A, B))