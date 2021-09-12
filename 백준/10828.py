# 백준 10828번 문제
# 스택

# push, pop, size, empty, top 기능을 가진 스택을 구현

n = int(input())

orders = []

for _ in range(n):
    orders.append(input())

stack = []

for i in range(n):
    order = orders[i].split()
    
    if order[0] == 'push':
        stack.append(int(order[1]))
    elif order[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            pop = stack.pop()
            print(pop)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif order[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            top = stack[-1]
            print(top)