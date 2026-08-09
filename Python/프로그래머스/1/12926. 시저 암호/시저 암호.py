def solution(s, n):
    code = []
    
    for i in s:
        if i == " ":
            new = " "
            
        elif "A" <= i <= "Z":           
            if ord(i) + n <= 90 :
                new = chr(ord(i)+n)
            else:
                new = chr(ord(i)+n-26)
                
        elif "a" <= i <= "z":
            if ord(i) + n <= 122 :
                new = chr(ord(i)+n)
            else:
                new = chr(ord(i)+n-26)
        
        code.append(new)
    
    answer = "".join(code)
    return answer