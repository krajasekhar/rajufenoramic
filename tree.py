# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    parArr=[]
    # root=None
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root==None:
            self.root=TreeNode(data)
            if data != -1:
                self.parArr.append(self.root)

        else:
            self.parent= self.parArr[0]
            if self.parent.left==None:
                node= TreeNode(data)
                self.parent.left=node
                if data != -1:
                    self.parArr.append(node)
                # else:

            else:
                if self.parent.right==None:
                    node= TreeNode(data)
                    self.parent.right=node
                    self.parArr.pop(0)
                    if data != -1:
                        self.parArr.append(node)
            
    def breadthFirstSearch(self):
        # node=self.root
        printArr=[]
        printArr.append(self.root)
        node=printArr.pop(0)
        while node != None:
            print(node.val)
            if node.val != -1:
                if node.left != None:
                    printArr.append(node.left)
                if node.right!= None:
                    printArr.append(node.right)
            # print(len(printArr))
            if len(printArr) > 0:
                node=printArr.pop(0)
            else:
                node = None
            
class Solution:
    # @param root : root node of tree
    # @param sum1 : integer
    # @return a list of list of integers

    def pathSum(self, root, sum1):
        pathArr=[[]]
        sumArr=[[0]]
        printArr=[]
        printArr.append(root)
        pathArr[0]=pathArr[0]+[root.val]
        node=printArr.pop(0)
        while node != None:
            # print(node.val)
            if node.val != -1:
                if node.left != None:
                    printArr.append(node.left)
                    if node.left.val != -1:
                        pathArr=pathArr+[pathArr[0]+[node.left.val]]
                if node.right!= None:
                    printArr.append(node.right)
                    if node.right.val != -1:
                        pathArr=pathArr+[pathArr[0]+[node.right.val]]
            # print(pathArr)
            if node.val != -1:
                tempArr=pathArr.pop(0)
                if node.left== None and node.right== None:
                    sumArr=sumArr+[tempArr]
                    # print(sumArr)
                else:
                    if node.left== None:
                        if node.right.val== -1:
                            sumArr=sumArr+[tempArr]
                            # print(sumArr)
                    if node.right== None:
                        if node.left.val== -1:
                            sumArr=sumArr+[tempArr]
                    if node.left!= None and node.right!= None:
                        if node.left.val== -1 and node.right.val== -1:
                            sumArr=sumArr+[tempArr]
            if len(printArr) > 0:
                node=printArr.pop(0)
                
            else:
                node = None
        # print(sumArr)
        resultArr=[]
        for i in range(0,len(sumArr)):
            if sum(sumArr[i])==sum1:
                resultArr=resultArr+[sumArr[i]]
        return resultArr

count = 11
ip1=[1, 2, 3, -1, -1, 4, -1, -1, 5, -1, 6]
# ip1=[1, 2, 3, 16, -1, 4, -1,-1,-1, -1, 5, -1, 6]
# ip1=[1, 2, 3, 4,5,6]
pathSum=19
tree= Tree()
#Insertion of data to the tree
for each in ip1:
    tree.insert(each)
#Breadth first search to see data
# tree.breadthFirstSearch()
sol = Solution()
output = sol.pathSum(tree.root,pathSum)
print(str(output))
