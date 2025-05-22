sequence = [5, -2, 9, 8, -3, -2, 4]
pos_nums = []
neg_nums = []
for num in sequence:
    if num > 0:
        pos_nums.append(num)
    if num < 0:
        neg_nums.append(num)

print(pos_nums[0])
print(neg_nums[-1])