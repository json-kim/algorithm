# 백준 1874번 문제
# 스택 수열

# 1부터 n까지의 수를 오름차순으로 스택에 push해간다.
# 중간중간 pop을 진행하며 만들어진 수열로 주어진 수열과 일치해야한다.
# 위의 작업을 수행하기 위한 push, pop의 조합을 출력.
# 불가능할 시 'NO'출력

n = int(input())
input_arr = []

for _ in range(n):
    input_arr.append(int(input()))

input_idx = 0
current_num = 1
stack = []
push_pop = []

while True:
    if current_num <= input_arr[input_idx]:
        stack.append(current_num)        
        current_num = current_num + 1
        push_pop.append('+')
    else:
        if len(stack) == 0: 
            if input_idx < n:
                print('NO')
                break
    
        if stack[-1] == input_arr[input_idx]:
            stack.pop()
            input_idx = input_idx + 1
            push_pop.append('-')
            if input_idx == n:
                for p in push_pop:
                    print(p)
                break
        else:
            print('NO')
            break