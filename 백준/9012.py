# 백준 9012번 문제
# 괄호

# VPS: 괄호가 바르게 쌍으로 이루어진 문자열
# 문자열이 주어졌을 때 VPS인지 판단 YES/NO 출력

t = int(input())
vps_input = []

for _ in range(t):
    vps_input.append(input())
    
    
for vps in vps_input:
    stack = []
    
    for i in range(len(vps)):
        if vps[i] == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                stack.append(')')
                break
            stack.pop()
            
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
        
