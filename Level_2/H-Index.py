def solution(citations):
    citations = sorted(citations)
    h_max = 0
    for i in range(1, len(citations) + 1):
        count = 0
        for j in range(len(citations)):
            if citations[j] >= i:
                count += 1
        if count >= i:
            h_max = i
    return h_max