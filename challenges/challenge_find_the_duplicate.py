def find_duplicate(nums):
    if (
        not nums
        or not isinstance(nums, list)
        or isinstance(nums, str)
        or len(nums) < 2
    ):
        return False

    if any(num < 1 for num in nums):
        return False

    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]

    return False
