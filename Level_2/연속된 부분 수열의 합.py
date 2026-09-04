def solution(sequence, k):
    start, end, total = 0, 0, sequence[0]
    best = [0, len(sequence) - 1]

    while start < len(sequence):
        if total < k:
            end += 1
            if end >= len(sequence):
                break
            total += sequence[end]
        elif total > k:
            total -= sequence[start]
            start += 1
        elif total == k:
            if (end - start) < (best[1] - best[0]):
                best = [start, end]
            total -= sequence[start]
            start += 1
    return best

# 앞에서 시작하는 투 포인터 문제