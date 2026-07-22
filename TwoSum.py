def twoSum(nums, target):
    Hmap = {}

    for i, n in enumerate(nums):
        diff = target - n

        if diff in Hmap:
            return [Hmap[diff], i]

        Hmap[n] = i

    return []

nums = [2, 7, 11, 15]
target = 9

result = twoSum(nums, target)
print(result)