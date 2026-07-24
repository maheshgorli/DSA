def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n

    # Prefix products
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    # Postfix products
    postfix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res


nums = list(map(int, input("Enter the array elements: ").split()))

answer = productExceptSelf(nums)


print("Output:", answer)