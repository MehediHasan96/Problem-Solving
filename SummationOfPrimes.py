
limit = 2000000
sum = 0
get_data = []
for i in range(1, limit+1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            get_data.append(i)

for data in get_data:
    sum += data
print(sum)
