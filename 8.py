ind = int(input())
a = []

for i in range(0, 201):
    if i < 10:
        a.append(i)
    elif 10 <= i <= 99:
        a.append(i // 10)
        a.append(i % 10)
    elif 100 <= i <= 200:
        a.append(i // 100)
        a.append((i // 10) % 10)
        a.append(i % 10)

print(a[ind-1])
