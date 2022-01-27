'''704. Binary Search
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''

def solution(array,target):
    if target not in array:
        return -1
    return array.index(target)


solution([-1,0,3,5,9,12] , -4)
