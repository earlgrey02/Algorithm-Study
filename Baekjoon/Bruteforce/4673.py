not_self_nums = set()

for i in range(1, 10001):
    not_self_nums.add(i + sum(map(int, str(i))))

for self_num in sorted(set(range(1, 10001)) - not_self_nums):
    print(self_num)