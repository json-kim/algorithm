# 백준 9461번 문제
# 파도반 수열 (동적 계획법)

# 파도처럼 나선형으로 삼각형을 추가한 도형에서 n번째 삼각형의 한변의 길이를 구하는 문제
# n번째 삼각형은 n-1, n-5번째 삼각형의 합이다.
# 따라서 처음 5개의 초기값은 입력해주어야 한다.
t = int(input())
testCase = []

for _ in range(t):
    testCase.append(int(input()))
    
triangle = [0] * (max(testCase)+6)
triangle[1] = 1
triangle[2] = 1
triangle[3] = 1
triangle[4] = 2
triangle[5] = 2

for i in range(6, max(testCase)+1):
    triangle[i] = triangle[i-1] + triangle[i-5]
    
for case in testCase:
    print(triangle[case])