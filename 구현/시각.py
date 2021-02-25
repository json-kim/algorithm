n = int(input())
inm = 10 + 6 - 1
inh = inm * 60 + inm * 60 - inm * inm
result = 0

for h in range(n+1):
    if(h % 3 == 0 and h != 0):
        result += 3600
    else:
        result += inh

print(result)
