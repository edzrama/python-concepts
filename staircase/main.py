def create_staircase(nums):
    step = 1
    subsets = []

    while nums:
        if len(nums) >= step:
            subsets.append(nums[:step])
            nums = nums[step:]
            step += 1
        else:
            return False

    return subsets


print(create_staircase([1, 2, 3, 4, 5, 6]))  