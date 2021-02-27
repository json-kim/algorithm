n = int(input())
array = []

for _ in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))


def getKey(data):
    return data[1]


#array = sorted(array, key=getKey)
array = sorted(array, key=lambda student: student[1])  # 람다 사용

for student in array:
    print(student[0], end=' ')
