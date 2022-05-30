##
# 05/30/2022
# Problem: Given an array of positive integers representing the values of coins in your possession, write a 
# function that returns the minimum amount of change that cannot be created.
# #

class Solution:
    def nonConstructibleChange(self,coins):
        #if coin value > changeAmount+1 then changeAmount+1 can't be created
        coins.sort()
        currentChangeAmount = 0

        for coin in coins:
            if coin > currentChangeAmount +1:
                return currentChangeAmount+1
            else:
                currentChangeAmount+=coin

        return currentChangeAmount+1

if __name__=="__main__":
    coins = [5,7,1,1,2,3,22]
    s = Solution()
    print(s.nonConstructibleChange(coins))

