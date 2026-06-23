# def solution(s):
    
#     while True:
#         for i in range(len(s) - 1):
#             if s[i] == s[i + 1]:
#                 s = s[:i] + s[i + 2:]
#                 break
#         else:
#             break

#     if len(s) == 0:
#         return 1
#     else:
#         return 0
    
    
# 스택으로 풀기    
def solution(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char: #len(stack) > 0 and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return 1 if not stack else 0