# 백준 11653번 문제
# 소인수분해

# n의 소인수 분해 결과를 한줄에 하나씩 출력
# 소수를 굳이 구할 필요가 없다.
# 2부터 시작하여 계속해서 나누어 떨어지면 계속 나누고
# 더이상 나누어 떨어지지 않으면 다음 숫자로 나누는 과정을 반복하면
# 2의 배수가 완전히 배제되고, 다음은 3의 배수가 배제되고 이 과정을 반복하는 것
n = int(input())

i = 2
while n > 1:
    # 소수로 나누어 떨어지면
    if n % i == 0:
        print(i)
        n = n // i
    else:
        i = i + 1