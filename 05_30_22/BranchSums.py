class Tree:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def branchSums(self,root):
        result = []
        self.dfs(root,0,result)
        return result
    
    def dfs(self,root,runningSum,result):
        if(root is None):
            return
        newSum = runningSum+root.value
        if(root.left==None and root.right==None):
            result.append(newSum)
            return
        self.dfs(root.left,newSum,result)
        self.dfs(root.right,newSum,result)
        

if __name__=='__main__':
    root = Tree(1)
    root.left = Tree(2)
    root.right = Tree(3)
    root.left.left = Tree(4)
    root.left.right = Tree(5)
    root.right.left = Tree(6)
    root.right.right = Tree(7)
    root.left.left.left = Tree(8)
    root.left.left.right = Tree(9)
    root.left.right.left = Tree(10)

    s = Solution()
    print(s.branchSums(root))


        
    