nums = list(range(1, 11))
numbers = len(nums)

sum_of_numbers = 0

while numbers > 0:
    sum_of_numbers += nums[numbers - 1]
    numbers -= 1

print(sum_of_numbers)

