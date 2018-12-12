'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, len(nums1), 1):
            nums1[i] = nums2[i - m]

        print(nums1)  # [1, 2, 3, 2, 5, 6]

        ### bubble sort!
        for i in range(len(nums1) - 1):
            for j in range(len(nums1) - i - 1):
                if nums1[j] > nums1[j + 1]:
                    nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j] #swap

        print(nums1)



solution = Solution()
print(solution.merge([1,2,3,0,0,0],3,[2,5,6],3))
'''
        for i in range(n):
            nums1[m+i]=nums2[i]
        print(nums1)

        #and then, sort
        nums1.sort()
'''