from collections import Counter

def solution(k, tangerine):
    counts = Counter(tangerine)
    sorted_counts = counts.most_common()

    total, answer = 0, 0
    for _, cnt in sorted_counts:
        if total >= k:
            break
        total += cnt
        answer += 1

    return answer

# Counter를 이용해야 하는 문제인데, sort를 할 땐 most_common으로.. (값, 갯수)로 나온다