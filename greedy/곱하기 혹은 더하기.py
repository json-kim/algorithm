s = input()
num = []

for i in range(len(s)):
    num.append(int(s[i]))

result = num[0]

for i in range(1, len(num)):
    if result+num[i] > result*num[i]:
        result += num[i]
    else:
        result *= num[i]

print(result)
