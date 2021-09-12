# 백준 10773번 문제
# 제로

# 정수를 기록하다가 0을 입력하면 가장 최근에 쓴 수를 지우기

k = int(input())
nums = []

for _ in range(k):
    input_num = int(input())
    
    if input_num == 0:
        nums.pop()
    else:
        nums.append(input_num)
        
print(sum(nums))
