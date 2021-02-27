array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 새로운 리스트를 리턴
result = sorted(array)
print(result)

# 기존의 리스트를 정렬
array.sort()
print(array)

# key를 활용한 정렬
array2 = [('바나나', 2), ('사과', 5), ('당근', 3)]


def setting(data):  # 정렬의 기준이 되는 key값을 리턴하는 함수
    return data[1]


result2 = sorted(array2, key=setting)  # key 매개변수로 함수를 입력
print(result2)
