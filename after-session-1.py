#Array: Largest Number ************************************
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def xLessThanY(self, x, y):
        xFirst = str(x) + str(y)
        yFirst = str(y) + str(x)
        
        if int(xFirst) < int(yFirst):
            return True
        
        else:
            return False
            
    def partition(self, A, start, end):
        pivot = A[end]
        pIndex = start
        
        for i in xrange(start, end):
            if self.xLessThanY(A[i], pivot):
                A[i], A[pIndex] = A[pIndex], A[i]
                pIndex += 1
        A[end], A[pIndex] = A[pIndex], A[end]
        return pIndex
        
    def quickSort(self, A, start, end):
        if start < end:
            p = self.partition(A, start, end)
            self.quickSort(A, start, p-1)
            self.quickSort(A, p+1, end)
        
    def largestNumber(self, A):
        strA = map(str, A)
        self.quickSort(strA, 0, len(strA)-1)
        answer = ''.join(reversed(strA))
        if int(answer) == 0:
          return "0"
        else: 
          return answer
        

#Array: Noble Integer ************************************
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        sortedA = sorted(A)
        
        for i in xrange(len(sortedA)):

            if sortedA[i] == len(sortedA)-1-i:
                
                if len(sortedA)-1-i == 0:
                  return 1
                
                for j in xrange(i+1, len(sortedA)):
                  if sortedA[j] == sortedA[i]:
                    break
                  
                  return 1
            
        return -1

#String: Reverse the String ************************************
class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        i = len(A) - 1
        retArr = []
        
        while (i>=0):
            while(i>=0 and A[i] == " "):
                i -= 1
            end = i
            
            while(i>=0 and A[i] != " "):
                i -= 1
            start = i
            
            retArr.append(A[start+1:end+1])
        
        reversedA = " ".join(retArr)
        return reversedA
    
#String: Implement StrStr ************************************
class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, haystack, needle):
        
        if haystack == None or needle == None:
            return -1
        
        if haystack == needle:
            return 0
        
        for i in xrange(len(haystack)-len(needle)):
            for j in xrange(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1
