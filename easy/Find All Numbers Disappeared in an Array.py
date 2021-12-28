'''448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2] 
'''

# solution
'''Note: 
we also have duplicates in array (use a set() to remove duplicates)
range is --->> [1,n] (key solution)
 1) set( range( 1,n+1) )
 2) for loop will give O(n) 
'''

def solution(array):
    num_len = len(array)
    the_range = set(range(1,num_len+1)) # [1,n]
    print(f'the range is {the_range}')
    for nums in array:
        print(f'num in array {nums}')
        if nums in the_range:
            the_range.remove(nums)
            print(the_range)
    print(list(the_range))


testing = [1,4,5,6]
solution(testing)
print('all products'.upper())