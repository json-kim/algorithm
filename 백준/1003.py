# 백준 1003번 문제
# 피보나치 함수(동적 계획법)

# 피보나치 함수를 호출했을 때 0과 1이 출력되는 횟수를 0부터 시작하여 차례대로 입력해가기
# 2일때의 값은 0일때, 1일때의 결과를 합치고,
# 3일때의 값은 1일때, 2일때의 결과를 합치는 식으로 계속해나가면된다.
t = int(input())
input_data = []

for _ in range(t):
    input_data.append(int(input()))
    
max_data = max(input_data)

count = []

# 입력이 0과 1일 때의 (0,1)호출값 추가
count.append((1,0))
count.append((0,1))

for i in range(2, max_data+1):
    count.append((count[i-1][0] + count[i-2][0],count[i-1][1] + count[i-2][1]))
    
for data in input_data:
    print(count[data][0], count[data][1])