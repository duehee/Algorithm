def solution(N, stages):
    arr = []
    answer = []
    for i in range(1, N+1):
        count = 0
        people = 0
        for stage in stages:
            if stage >= i:
                count += 1
            if stage == i:
                people += 1
        if count == 0:
            fail = 0
        else:
            fail = people / count
        arr.append((fail, i))
    arr = sorted(arr, key=lambda arr:arr[0], reverse = True)
    for i in range(len(arr)):
        answer.append(arr[i][1])

    return answer