def solution(n, words):
    count, cool = 1, 0
    used_word = set()
    used_word.add(words[0])
    while 1:
        if count == len(words):
            cool = 1
            break
        if words[count] not in used_word and words[count-1][-1] == words[count][0] and (len(words[count]) > 1):
            used_word.add(words[count])
            count += 1
        else:
            break
    if cool == 1:
        return [0, 0]
    else:
        return [count % n + 1, count // n + 1]