from collections import deque


def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    count = 0

    while queue:
        current = queue.popleft()

        if any(q[1] > current[1] for q in queue):
            queue.append(current)
        else:
            count += 1
            if current[0] == location:
                return count

# [0, 1, 2, 3] [2, 1, 3, 2]  count = 0 location = 2
# [1, 2, 3, 0] [1, 3, 2, 2]  그냥.. 넘겨
# [2, 3, 0, 1] [3, 2, 2, 1]  count = 1, current[0] = location이니까 count 뱉기