# 백준 1541번 문제
# 잃어버린 괄호

# 괄호를 친다 = 연산의 우선순위를 매긴다
# 연산의 우선순위 변경에 따른 결과값이 최솟값이 되도록 괄호를 배치
# 뺄셈을 나중에 하는게 좋아보인다
# 방법 1 먼저 덧셈을 전부 다 하고 뺄셈을 하는건 어떨까?
# 이 방법이라면 덧셈, 뺄셈연산들 안에서는 순서가 상관없다. 단지 덧셈만 먼저하면 된다.
def findOperator(exp):
    oper = []
    num = ''
    for e in exp:
        if e != '-' and e != '+':
            num = num + e
        else:
            oper.append(e)
    return oper, oper.count('-')

def findNums(exp):
    nums = []
    compExp = exp.split('-')
    for e in compExp:
        nums.extend(map(int,e.split('+')))
    return nums
    
expression = input()

# 숫자, 연산자들을 따로 리스트로 구분(순서대로)
nums = findNums(expression)
operators, minusN = findOperator(expression)

i = 0
# 덧셈만 우선 수행
while len(operators) > minusN:
    oper = operators[i]
    if oper == '+':
        # 해당 위치 숫자들 덧셈 수행
        nums[i] = nums[i] + nums[i+1]
        del nums[i+1]
        # 사용한 연산자 제거
        del operators[i]
    else:
        # 뺄셈은 건너뛰기
        i = i + 1
    
# 나머지 뺄셈 수행    
while len(operators) > 0:
    # 남은 숫자들 뺄셈 수행
    nums[0] = nums[0] - nums[1]
    del nums[1]
    # 사용한 연산자 제거
    del operators[0]
    

print(nums[0])
        