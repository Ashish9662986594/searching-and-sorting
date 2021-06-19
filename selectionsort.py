def sort(nums):

    for i in range(5):            # we going to index lowest to high so 0 to 5
        minpos = i
        for j in range(i,6):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)

nums = [45, 78, 3, 567, 34, 2]
sort(nums)

print(nums)