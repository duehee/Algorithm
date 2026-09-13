def solution(n,a,b):
    round_num = 0

    while a != b:
        a = (a + 1) // 2 # 2 1 1
        b = (b + 1) // 2 # 4 2 1 이라 서 ..
        round_num += 1

    return round_num