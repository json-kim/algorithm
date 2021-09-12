# 백준 1931번 문제
# 회의실 배정(그리디)

# 그리디: 매순간 가장 좋은걸 선택
# 가장 좋은 회의는 빨리 끝나는 회의
# 끝나는 시간을 기준으로, 시작하는 시간을 두번째 기준으로 삼고 정렬
n = int(input())
schedule = []
count = 1

for _ in range(n):
    s, e = map(int, input().split())
    schedule.append((s, e))
    

schedule = sorted(schedule, key=lambda x: (x[1], x[0]))

end_time = schedule[0][1]

for sch in schedule[1:]:
    if end_time <= sch[0]:
        end_time = sch[1]
        count = count+1

print(count)