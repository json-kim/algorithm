import heapq
hq = []
k = int(input())
food_times = list(map(int, input().split()))
n = len(food_times)
# 입력값을 튜플로 바꾸어 시간을 기준으로 정렬
input_tuple = []
for i in range(1, n+1):
    heapq.heappush(hq, (food_times[i-1], i))
print(hq)
per_time = 0

while hq:
    use_time = (hq[0][0] - per_time) * len(hq)
    if use_time <= k:
        k -= use_time
        per_time = hq[0][0]
        while hq[0][0] == per_time:
            heapq.heappop(hq)
    else:
        hq.sort(key=lambda x: x[1])
        print(hq[k % len(hq)][1])
        break
