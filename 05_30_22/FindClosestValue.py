from turtle import left

from matplotlib.pyplot import close


class Tree:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def findClosestBST(self,tree,target):
        return self.inOrderSearch(tree,target,tree.value)

    def inOrderSearch(self,tree,target,closest):
        if(tree):
            if(abs(tree.value-target)<abs(target-closest)):
                closest = tree.value
            if(target<tree.value):
                return self.inOrderSearch(tree.left,target,closest)
            elif(target>tree.value):
                return self.inOrderSearch(tree.right,target,closest)
            else:
                return closest
        else:
            return closest