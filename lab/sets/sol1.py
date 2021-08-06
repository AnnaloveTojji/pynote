# Given an array of integers, verify if the array contains any duplicates. 
# The function should return true if any value appears at least twice in the array, 
# or false if every element is distinct.

#Input: [3,3,1,2,6,4,1,2,4,5]
#Output: true
#Input: [1,2,3,4]
#Output: false

nums = [21, 13, 35, 31, 12, 35, 10, 9, 9]

def solution(nums):
    return True if len(set(nums)) < len(nums) else False

solution(nums)