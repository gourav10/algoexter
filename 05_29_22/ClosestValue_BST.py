from cgitb import lookup
from lib2to3.pytree import Node

from sympy import root


class BST:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def findClosestValueInBst(self,tree,target):
        numList=[]

        def inOrder(root,numList):
            if(root):
                inOrder(root.left)
                numList.append(root.value)
                inOrder(root.right)
        
        inOrder(tree,numList)
        result = []
        min_diff = float('inf')
        for num in numList:
            diff = abs(target-num)
            if(min_diff>diff):
                result.append(num)
                min_diff = diff
            
        return result