num_list = list(map(int, input().split()))

prev_sum = 0
new_list = []

for i in num_list:
    prev_sum = i + prev_sum
    new_list.append(prev_sum)

print(new_list)





