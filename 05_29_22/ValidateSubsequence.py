class Solution:
    def isValidSubsequence(self,array,sequence):
        j=0
        for i in range(len(array)):
            if j==len(sequence):
                break
            if(array[i]==sequence[j]):
                j+=1
        
        return j==len(sequence)

if __name__=='__main__':
    array = [5,1,22,25,6,-1,6,10]
    seq = [22, 25, 6]

    s = Solution()

    print(s.isValidSubsequence(array,seq))
