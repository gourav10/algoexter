class Solution:
    def threeNumberSum(self,array,targetSum):
        array.sort()
        result = []
        for currIdx in range(len(array)-2):
            left = currIdx+1
            right = len(array)-1
            while(left<right):
                tSum = array[currIdx]+array[left]+array[right]
                if tSum==targetSum:
                    result.append([array[currIdx],array[left],array[right]])
                    left+=1
                    right-=1
                    
                elif(tSum<targetSum):
                    left+=1
                else:
                    right-=1
        return result

if __name__=='__main__':
    array= [12,3,1,2,-6,5,-8,6]
    targetSum = 0
    s = Solution()
    print(s.threeNumberSum(array,targetSum))
                