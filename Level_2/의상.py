from collections import Counter


def solution(clothes):
    categories = [item[1] for item in clothes]
    count = Counter(categories)

    answer = 1
    for category in count.values():
        answer *= (category + 1)

    return answer - 1

# Counter에서 categories 뽑는 걸 좀 고민했다