"""53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

"""
# hint : kadane's algorithm  : - Finding maximum subarray sum for a given array of integer

def solution(array):
    max_no = array [0]
    max_sum = 0
    for n in array:
        if max_sum < 0 :
            max_sum = 0
        max_sum += n
        max_no = max(max_sum,max_no)
    return max_no

print(solution([-2,1,-3,4,-1,2,1,-5,4]))