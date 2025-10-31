def permuteUnique(nums):
    nums.sort()
    result=[]
    def helper(nums,i):
        if i ==len(nums):
            if nums not in result:
                result.append(nums[:])
            return


        for j in range(i,len(nums)):
            # while i <len(nums) and nums[i]==nums[i-1]:
            #     i+=1
            nums[i],nums[j]=nums[j],nums[i]
            helper(nums,i+1)
            nums[i],nums[j]=nums[j],nums[i]
    helper(nums,0)
    return result
