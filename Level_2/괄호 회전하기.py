def solution(s):
    double_s = s * 2
    answer = 0
    for i in range(len(s)):
        s_list = double_s[i:i+len(s)]
        stack = []
        for ch in s_list:
            if len(stack) == 0:
                stack.append(ch)
            elif stack[-1] == '(' and ch == ')':
                stack.pop()
            elif stack[-1] == '{' and ch == "}":
                stack.pop()
            elif stack[-1] == '[' and ch == "]":
                stack.pop()
            else:
                stack.append(ch)
        if len(stack) == 0:
            answer += 1
    return answer

# 스택 문제