class Solution:
    def nonConstructibleChange(self,coins):
        change = 0
        coins.sort()
        for coin in coins:
            if(coin>change+1):
                return change+1
            else:
                change+=coin
        return change+1

if __name__=="__main__":
    coins = [1,2,5]
    s = Solution()
    print(s.nonConstructibleChange(coins))