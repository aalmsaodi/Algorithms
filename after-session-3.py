#BST: Implement Power Function *********************************
class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        
        if n == 0:
            return 1 % d

        ans = 1
        base = x
    
        while n > 0:
            if n % 2 == 1:
                ans = ans*base % d
                n -= 1
            else:
                base = base*base % d
                n /= 2
    
        return ans
        
#BST: Matrix Search *********************************
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
        if A == None or len(A) == 0:
            return 1
        
        if len(A) == 1:
            return self.binarySearch(A[0], B)
        
        for row in A:
            if B >= row[0] and B <= row[len(row)-1]:
                return self.binarySearch(row, B)
        
        return 0

#Trees: Identical Binary Trees ************************************
class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if A == None or B == None:
            if A == B:
                return True
            else:
                return False
        
        
        if A.val == B.val:
            return self.isSameTree(A.left, B.left) and self.isSameTree(A.right, B.right)
        else:
            return False


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
        
