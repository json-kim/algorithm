# 백준 4949번 문제
# 균형잡힌 세상

# (), [] 괄호의 균형이 잘 맞는지 판단
# 모든 오른쪽 괄호는 자신의 짝(왼쪽 괄호)가 존재

sentences = []

while True:
    input_str = input()
    
    if len(input_str) == 1 and input_str[0] == '.':
        break
    
    if input_str[-1] == '.':
        sentences.append(input_str)
    else:
        sentences[-1] = sentences[-1] + input_str
        
for sentence in sentences:
    stack = []
    
    for i in range(len(sentence)):
        if sentence[i] == '(':
            stack.append('(')
        elif sentence[i] == '[':
            stack.append('[')
        elif sentence[i] == ')':
            if len(stack) == 0:
                stack.append(')')
                break
            if stack[-1] != '(':
                break
            stack.pop(-1)
        elif sentence[i] == ']':
            if len(stack) == 0:
                stack.append(']')
                break
            if stack[-1] != '[':
                break
            stack.pop(-1)
    
    if len(stack) != 0:
        print('no')
    else:
        print('yes')