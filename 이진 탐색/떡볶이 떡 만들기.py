n, m = map(int, input().split())
input_data = list(map(int, input().split()))
input_data.sort()
result = max(input_data)


def binary_search(array, min, max):
    print(min, max)
    if max == min:
        return max
    mid = (min + max) // 2
    sum = 0
    for i in array:
        if mid < i:
            sum += i - mid

    if sum == m:
        return mid
    elif sum < m:
        return binary_search(array, min, mid-1)
    else:
        return binary_search(array, mid+1, max)


print(binary_search(input_data, 0, input_data[n-1]))
