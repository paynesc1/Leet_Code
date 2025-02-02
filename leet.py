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
    
    def Traverse(self, l1, l2):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        #Iterating through each list and adding values
        while l1 or l2:
            val1 = l1.data
            val2 = l2.data
            sum = val1 + val2 + carry
            if sum > 9:
                sum = 10 - sum
                carry = 1

            current.next = ListNode(sum)

            #move to next node
            l1 = l1.next
            l2 = l2.next
            
            print(current.next.data)

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))


solution = ListNode()
result = solution.Traverse(l1, l2)