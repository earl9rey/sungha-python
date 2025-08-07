nums = list(map(int, input().split()))
ascend = [1, 2, 3, 4, 5, 6, 7, 8]
decend = sorted(ascend, reverse=True)

if nums == ascend :
    print("ascending")
elif nums == decend :
    print("descending")
else :
    print("mixed")