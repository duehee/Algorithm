def solution(arr1, arr2):
    n = len(arr1)  # arr1의 행 길이
    m = len(arr2[0])  # arr2의 열 길이
    k_len = len(arr2)  # arr1의 열 갯수 = arr2의 행 갯수
    answer = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            total = 0
            for k in range(k_len):
                total += arr1[i][k] * arr2[k][j]
            answer[i][j] = total
    return answer

# 머리가 안 굴러가잉