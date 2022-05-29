from tkinter.tix import Tree
from unicodedata import name


class Solution:
    # TC: O(n) | SC: O(n)
    def twoNumberSum(self,array,targetSum):
        lookUp  = {}

        for num in array:
            diff = targetSum - num
            if(diff in lookUp):
                lookUp[diff] = True
                return [diff,num]
            else:
                lookUp[num] = True
        return []

    def twoNumberSumNonHash(self,array,targetSum):
        array.sort() # T.C: O(nlog n)
        left = 0
        right = len(array)-1
        while(left!=right):
            curr_sum = array[left]+array[right]
            if(curr_sum==targetSum):
                return [array[left],array[right]]
            elif curr_sum<targetSum:
                left+=1
            elif curr_sum>targetSum:
                right+=1
        return []

if __name__ == "__main__":
    s = Solution()
    array = [3,5,-4,8,11,1,-1,6]
    targetSum = 10
    print("XYZ")
    print(s.twoNumberSumNonHash(array,targetSum))