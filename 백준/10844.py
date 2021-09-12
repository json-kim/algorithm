# 백준 10844번 문제
# 쉬운 계단 수 (동적 계획법)

# 인접한 모든 숫자의 차이가 1인 수 ex)45656
# 길이가 n인 계단수의 숫자를 구하는 문제
# 자릿수를 한칸씩 늘려가며 마지막 숫자를 가지고 다음에 올 숫자의 갯수를 계산할 수 있다.
# 그리고 예상 숫자들의 합이 n자릿수를 가진 계단수의 가능 가짓수이다.
# 결국 끝자릿수만 가지고 한칸씩 늘려가며 가짓수를 계산할 수 있다.

# 현재 끝자리 수를 가지고 다음에 올 숫자들을 구하는 함수
def getNext(nums):
    result = [0] * 10
    for i in range(10):
        if i == 0:
            result[1] = result[1] + nums[i]
        elif i == 9:
            result[8] = result[8] + nums[i]
        else:
            result[i-1] = result[i-1] + nums[i]
            result[i+1] = result[i+1] + nums[i]
    return result

n = int(input())

nums = []
nums.append([0,1,1,1,1,1,1,1,1,1])

for i in range(n-1):
    nums.append(getNext(nums[i]))
    
print(sum(nums[-1])%1000000000)