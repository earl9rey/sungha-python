def solution(n, arr1, arr2):
    answer = []
    b1, b2 = [], []

    for i in arr1:
        b1.append(bin(i)[2:].zfill(n))

    for i in arr2:
        b2.append(bin(i)[2:].zfill(n))

    for i in range(n):
        line = ""

        for j in range(n):
            if b1[i][j] == "1" or b2[i][j] == "1":
                line += "#"
            else:
                line += " "

        answer.append(line)

    return answer