def sort(nums):
    for i in range(len(nums)-1,0,-1):   #here i is  outer loop, len(nums) is a list -1 is stand for nums value to start the 0 the list
                                        # 0 stand for order like here list contain 7 value so 7 to 0 
                                         # When we going to negative order so we take -1 for iteration
         
         for j in range(i):             
            if nums[j]>nums[j+1]:       # This is a swap when the 1 value is > 2 value then 
                temp = nums[j]          #This is a swapping
                nums[j] = nums[j+1]
                nums[j+1] = temp 

nums = [1,45,6,2,57,78,2]
sort(nums)

print(nums)