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
# Psuedo Explanation
# iterate through each value in the list
# add number for List 1 with Number from List 2
# If sum exceeds 10, create a variable for the remainder above
# add the carry over variable tot he sume of the next two digits
# return the final number as a linked list

# Definition for singly-linked list.
class ListNode():
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
    
    def Traverse(head):
        print("Success")
        print(head)
        current = head
        while current is not None:
            # print(current.data)
            current = current.next
            print(current)

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))


solution = ListNode()
print(solution.Traverse())