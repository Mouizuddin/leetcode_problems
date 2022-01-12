'''1470. Shuffle the Array

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1 :
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

Example 2 :
Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]

Example 3 :
Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]

Constraints:
1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3
'''

# solution
'''Algorithm 
1) divide the array into two half's [X1,Y1,.....Xn,Yn]
2) first half X1 to and second half to Y1
3) result.append(X1, Y1)
'''
# solution 1
def shuffle(nums, n=0) :
    n = len(nums) // 2
    j = n
    output = []
    for i in range(n) :# [0,1,2]
        output.append(nums[i])
        output.append(nums[j])
        j += 1 # [3,4,5]
    return output

# solution 2
def solution_2(array):
    result = []
    for i in range(len(array) // 2):
        result.append(array[i])
        result.append(array[i + len(array) // 2])
    return result

'''
Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]
'''
solition_1 = shuffle([1,2,3,4,4,3,2,1])
print(solition_1)
print('===='*10)
solition_1 = solution_2([1,2,3,4,4,3,2,1])
print(solition_1)