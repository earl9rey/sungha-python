# def solution(s):
    
#     result = []
#     i = 0
    
#     while True:
#         if len(s) == len(result):
#             break
            
#         if s[i] == " ":
#             result.append(" ")
#             i = 0
#             continue
        
#         if i % 2 == 0:
#             result.append(s[i].upper())
#         else:
#             result.append(s[i].lower())
            
#         i += 1
        
            
#     answer = ''.join(result)
#     return answer

def solution(s):
    result = []
    index = 0

    for i in s:
        if i == ' ':
            result.append(' ')
            index = 0
            
        else:
            if index % 2 == 0:
                result.append(i.upper())
            else:
                result.append(i.lower())
                
            index += 1

    return ''.join(result)