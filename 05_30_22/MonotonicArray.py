class Solution:
    def isMonotonic(self,array):
        
        nonDecreasing = self.isNonDecreasing(array)
        nonIncreasing = self.isNonIncreasing(array)
        if(not nonIncreasing and not nonDecreasing):
            return False
        return True

    def isNonDecreasing(self,array):
        for i in range(1,len(array)):
            if(array[i-1]>array[i]):
                return False
        return True
    
    def isNonIncreasing(self,array):
        for i in range(1,len(array)):
            if(array[i-1]<array[i]):
                return False
        return True

if __name__=='__main__':
    # array = [-1,-5,-10,-1100,-1100,-1101,-1102,-9001]
    array = []
    s = Solution()
    print(s.isMonotonic(array))
