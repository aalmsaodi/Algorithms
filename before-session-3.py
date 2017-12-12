#Trees: Vertical Order traversal of Binary Tree *********************************
class Solution:
    
    def insertTreeToDict(self,tree,width,height,dic):
        if tree == None:
            return dic
        
        if width in dic:
            dic[width].append((height, tree.val))
        else:
            dic[width] = [(height, tree.val)]
            
        dic = self.insertTreeToDict(tree.left,width-1, height+1, dic)
        dic = self.insertTreeToDict(tree.right,width+1, height+1, dic)
        return dic
        
    def verticalOrderTraversal(self, A):
        dic = self.insertTreeToDict(A,0,0,{})
        result =[]
        
        for i in sorted(dic):
            y = dic[i]
            y.sort(key=lambda x: x[0])
            result.append([x[1] for x in y])
        return result

#Trees: Balanced Binary Tree ************************************
class Solution:
    def depth (self, tree):
        if (tree == None):
            return 0
        return max(self.depth(tree.left), self.depth(tree.right)) + 1

    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        if (A == None):
            return True
        
        l = self.depth(A.left)
        r = self.depth(A.right)
        
        return abs(l-r) <= 1 and self.isBalanced(A.left) and self.isBalanced(A.right)


#Hashing: Matrix Search ************************************
class Solution:
    
    def binarySearch(self, flatA, B):
        if len(flatA) == 1:
            if flatA[0] == B:
                return 1
            else:
                return 0
        
        mid = len(flatA)/2
        
        if B >= flatA[mid]:
            return self.binarySearch(flatA[mid:], B)
        else:
            return self.binarySearch(flatA[:mid], B)
    
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        if len(A) == 1:
            return self.binarySearch(A[0], B)
        
        mid = len(A)/2
        
        if B >= A[mid][0]:
            self.searchMatrix(A[mid:], B)
        else:
            self.searchMatrix(A[:mid], B)
