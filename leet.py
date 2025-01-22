""" ***Leet Code Problem #1 *** """
# class Solution:
#     def twoSum(self, data, target):
#         for i in range(len(data)):
#             for j in range(i+1, len(data)):
#                 if data[i] + data[j] == target:
#                     return[i,j]
                
# solution = Solution()
# # print(solution.twoSum([3,2,4], 6))
# print(solution.twoSum([2,7,11,15], 9))


""" *** Improved Time Complexity *** """
# Improved time complexity using enumerate()
# class Solution:
#     def twoSum(self, data, target):
#         lookup = {}
#         for i, num in enumerate(data):
#             final = target - num
#             if final in lookup:
#                 return[lookup[final], i]
#             lookup[num] = i
                
# solution = Solution()
# # print(solution.twoSum([2,7,11,15], 9))
# print(solution.twoSum([3,3],6))



""" *** Leet Code Problem 2 *** """
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        