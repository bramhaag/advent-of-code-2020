with open('input.txt') as file:
    nums = [int(x) for x in file.read().splitlines()]


num_length = 25

for i, num in enumerate(nums[num_length:]):
    last_nums = nums[i:i+num_length]

    if num not in {x+y for x in last_nums for y in last_nums}:
        print(f"Part 1: {num}")
        break

for i in range(len(nums)):
    s = mi = ma = nums[i]
    for j in range(i+1, len(nums)):
        n = nums[j]
        s += n

        if mi > n: mi = n
        if ma < n: ma = n
        
        if s == num:
            print(f"Part 2: {mi+ma}")
            break
        elif s > num:
            break
