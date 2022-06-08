#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#Input: nums = [1,2,3,1]
#Output: true

def doubles(nums):
    for x in nums:
        if nums.count(x) > 1:
            return True

    return False

print(doubles([1,2,3,1]))
print(doubles([1,2,3]))