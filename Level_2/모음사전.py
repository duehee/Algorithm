def solution(word):
    alp_list = ['A', 'E', 'I', 'O', 'U']
    count = 0
    answer = 0

    def dfs(current):
        nonlocal count, answer

        if len(current) != 0:
            count += 1

        if current == word:
            answer = count

        if len(current) < 5:
            for alp in alp_list:
                dfs(current + alp)

    dfs("")
    return answer