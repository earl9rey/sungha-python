# def solution(s):
#     s = s.lower()
#     jaden = list(map(str, s.split()))
        
#     for i in range(len(jaden)):
#         if jaden[i][0].isdigit() == True:
#             continue
#         else:
#             jaden[i] = jaden[i][0].upper() + jaden[i][1:]
    
#     answer = " ".join(jaden)
    
#     return answer

# 공백 문자가 연속해서 나올 수 있음

def solution(s):
    s = s.lower()
    jaden = list(map(str, s.split(" ")))
        
    for i in range(len(jaden)):
        if jaden[i] == "":
            continue
            
        if jaden[i][0].isdigit() == True:
            continue
        else:
            jaden[i] = jaden[i][0].upper() + jaden[i][1:]
    
    answer = " ".join(jaden)
    
    return answer