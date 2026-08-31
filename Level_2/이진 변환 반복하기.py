def solution(s):
    remove_zero_count = 0
    convert_count = 0

    while s != "1":
        remain_one = s.count('1')
        remove_zero_count += s.count('0')
        s = bin(remain_one)[2:]
        convert_count += 1

    return [convert_count, remove_zero_count]

## count 잘 쓰면 편했던 문제