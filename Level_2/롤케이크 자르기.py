from collections import Counter

def solution(topping):
    set_a = set()
    set_b = Counter(topping)
    set_b_count = len(set_b)
    answer = 0

    for t in topping:
        set_a.add(t)
        set_b[t] -= 1
        if set_b[t] == 0:
            set_b_count -= 1

        if len(set_a) == set_b_count:
            answer += 1

    return answer