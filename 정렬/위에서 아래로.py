n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array.sort()
array.reverse()
#result = array[::-1]
print(array)
