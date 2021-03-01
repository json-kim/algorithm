n = int(input())
products = list(map(int, input().split()))

m = int(input())
orders = list(map(int, input().split()))

result = ['no'] * m
result2 = ['no'] * m
result3 = ['no'] * m
result4 = ['no'] * m

# 순차 탐색
for i in range(m):
    for j in range(n):
        if orders[i] == products[j]:
            result[i] = 'yes'

print(result)


# 이진 탐색
products.sort()


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


for i in range(m):
    if binary_search(products, orders[i], 0, n-1) != None:
        result2[i] = 'yes'

print(result2)


# 계수 정렬 이용
array = [0] * (max(products) + 1)

for product in products:
    array[product] += 1

for i in range(m):
    if array[orders[i]] > 0:
        result3[i] = 'yes'

print(result3)


# 집합 자료형 이용
array2 = set(products)

for i in range(m):
    if orders[i] in array2:
        result4[i] = 'yes'

print(result4)
