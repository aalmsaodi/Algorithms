#Checkpoint: Level 2 ************************************
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        size = (A*2) -1
        arr = [[0 for x in xrange(size)] for y in xrange(size)]
        
        for i in xrange(0, size):
            for j in xrange(i , size-i):
                arr[i][j] = A-i
                arr[j][i] = A-i
                arr[size-i-1][j] = A-i
                arr[j][size-i-1] = A-i
        return arr

#Checkpoint: Level 3 ************************************
#Kth Smallest Element in the Array
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
            
    def kthsmallest(self, A, k):
        newA = list(A)
        newA = self.sortMerge(newA)
        return newA[k-1]

    def sortMerge(self, A):
        n = len(A)
        if (n<2):
            return A
        mid = n//2
        left = A[:mid]
        right = A[mid:]
        l = self.sortMerge(left)
        r = self.sortMerge(right)
        return self.merge(l, r)
    
    def merge(self, left, right):
        A = list()
        i,j = 0,0
        
        while (i<len(left) and j<len(right)):
            if left[i] < right[j]:
                A.append(left[i])
                i += 1
            else:
                A.append(right[j])
                j += 1

        while (i<len(left)):
            A.append(left[i])
            i += 1

        while (j<len(right)):
            A.append(right[j])
            j += 1
        return A
    
#NUMRANGE
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
        size = len(A)
        count, currentSum = 0, 0
        startIndex, i = 0, 0
        
        while(startIndex < size):
            currentSum += A[i]
            if (B <= currentSum <= C):
                count += 1
            elif (currentSum > C):
                currentSum = 0
                i = startIndex
                startIndex += 1
            
            i += 1
            if (i == size) :
                currentSum = 0
                startIndex += 1
                i = startIndex
            
        return count

#Checkpoint: Level 4 ************************************
#SUBTRACT 
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        valuesArr = []
        tempHead = A
        
        while (tempHead is not None):
            valuesArr.append(tempHead.val)
            tempHead = tempHead.next
        tempHead = A
        for i in xrange(len(valuesArr)/2):
            tempHead.val = valuesArr[len(valuesArr)-1-i] - tempHead.val
            tempHead = tempHead.next
        return A

#NEXTGREATER
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        for i in xrange(len(A)):
            currentGreater = A[i]
            j = i + 1
            next = -1
            while (j < len(A)):
                if A[i] < A[j]:
                    next = A[j]
                    break
                j += 1
            A[i] = next
        return A

#Checkpoint: Level 5 ************************************
#All Unique Permutations
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        if len(A) <= 1 :
            return [A]
        else:
            retArr = []
            uniqueElements = set(A)
            for x in uniqueElements:
                tempA = list(A)
                tempA.remove(x)
                for p in self.permute(tempA):
                    retArr.append([x] + p)
            return retArr

#Longest Consecutive Sequence
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        
        currentCount = 0
        maxCount = 0
        
        sequence = set(A)
        
        for element in sequence:
            
            if element-1 not in sequence:
                currentElement = element
                currentCount = 1
                
                while currentElement+1 in sequence:
                    currentElement += 1
                    currentCount += 1
                
                maxCount = max(maxCount, currentCount)
        
        return maxCount