# Given two arrays, write a function to compute their intersection. 
# Each element in the result must be unique and the result can be unordered.

# Example 1:
# Input: nums1 = [2,3,3,2], nums2 = [3,3]
# Output: [3]
# Example 2:
# Input: nums1 = [5,7,4], nums2 = [5,7,5,8,5]
# Output: [5,7]

nums1 = [3, 5, 7, 10, 9]
nums2 = [7, 11, 2, 17, 5]

# Solution using the intersection operator:
def solution_one(nums1, nums2):
    return list(set(nums1) & set(nums2))
  
# Or alternatively using the intersection method (faster & less memory):
def solution_two(nums1, nums2):
    return list(set(nums1).intersection(nums2))

print(solution_one(nums1, nums2))
print(solution_two(nums1, nums2))