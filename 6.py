n, k, m = map(int, input().split())
time = 0

time += (m * (n // k)) * 2
if n % k != 0:
    if k // (n % k) >= 2:
        time += m
    else:
        time += m * 2
print(time)
