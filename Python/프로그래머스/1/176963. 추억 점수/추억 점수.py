def solution(name, yearning, photo):
    # score = {}

    # for i in range(len(name)):
    #     score[name[i]] = yearning[i]
    score = dict(zip(name, yearning))

    answer = []

    for people in photo:
        total = 0

        for person in people:
            if person in score:
                total += score[person]

        answer.append(total)

    return answer