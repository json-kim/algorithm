s = input()
num = []
count = 0

for i in s:
    num.append(int(i))

n = num[0]


def change(num, start, end):
    for i in range(start, end+1):
        num[i] = (num[i] + 1) % 2


def reverse_string():
    global count
    left = 0
    right = len(num) - 1

    while True:
        while num[left] == n and left < len(num) - 1:
            left += 1
        while num[right] == n and right > 0:
            right -= 1

        if left > right:
            break

        change(num, left, right)
        count += 1


reverse_string()

print(count)
