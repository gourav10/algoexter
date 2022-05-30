from numpy import array


class Solution:
    def smallestDifference(self,arrayOne,arrayTwo):
        arrayOne.sort()
        arrayTwo.sort()

        idx1 = 0
        idx2 = 0

        minDiff = float('inf')
        
        while idx1<len(arrayOne) and idx2<len(arrayTwo):
            diff = abs(arrayOne[idx1] - arrayTwo[idx2])
            if(diff<minDiff):
                minDiff = diff
            

