from collections import deque

def solution(s):
    answer = 0
    
    for i in range(0, len(s)):
        r = rotate(s, i)
        
        if isRight(r) == True:
            answer += 1
        
    return answer


def rotate(s, x):
    rotated = s[x:] + s[:x]
    return rotated
    

def isRight(s):
    stack = deque()

    for c in s:
        if c in "([{":
            stack.append(c)
        else:
            if not stack:
                return False

            if c == ")" and stack[-1] != "(":
                return False
            if c == "]" and stack[-1] != "[":
                return False
            if c == "}" and stack[-1] != "{":
                return False

            stack.pop()

    return len(stack) == 0