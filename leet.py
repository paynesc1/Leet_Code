# class Solution:
#     def twoSum(self, data, target):
#         for i in range(len(data)):
#             for j in range(i+1, len(data)):
#                 if data[i] + data[j] == target:
#                     return [i,j]

class Solution:
    def twoSum(self, data, target):
        for i in range(len(data)):
            for j in range(i+1, len(data)):
                if data[i] + data[j] == target:
                    return[i,j]
solution = Solution()
print(solution.twoSum([3,2,4], 6))
#for value in list, starting at zero
#add two value togeth to get target
#3 add 
            
