def solution(n):
    count = 0
    start, end = 1, 1
    total = 1

    while start <= n:
        if total == n:
            count += 1
            total -= start
            start += 1
        elif total < n:
            end += 1
            total += end
        else:
            total -= start
            start += 1

    return count

## 전형적인 투포인터 문제인데 먼가 생각이 잘 안났음