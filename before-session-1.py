#Array: Add One To Number ************************************
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        strA = map(str, A)
        resultInt = int(''.join(strA)) + 1
        resultStr = str(resultInt)
        return (list(resultStr))

#Array: Max Non Negative SubArray ************************************
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        i = 0
        maxSum = -1
        ret = []
        
        while i < len(A):
            tempArr = []
            while i < len(A) and A[i] >= 0:
                tempArr.append(A[i])
                i += 1
            
            if (sum(tempArr) > maxSum):
                ret = tempArr
                maxSum = sum(tempArr)
            i += 1
        return ret

#String: Length of Last Word ************************************
class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        beginningWordIndex = 0
        endingWordIndex = -1
        i = len(A)-1
        
        while(i >= 0 and A[i] == " "):
                i -= 1
        endingWordIndex = i
            
        while(i >= 0 and A[i] != " "):
                i -= 1
        beginningWordIndex = i        
            
        return endingWordIndex - beginningWordIndex
    
#String: Longest Common Prefix ************************************
class Solution:
    # @param A : list of strings
    # @return a strings
    
    def twoPrefix(self, a, b):
        i = 0
        while i <  min(len(a), len(b)) and a[i] == b[i]:
            i += 1
  
        if i > min(len(a), len(b)):
            return a[:i+1]
        else:
            return a[:i]
    
    def longestCommonPrefix(self, A):
        common = A[0]
  
        for i in xrange(1,len(A)):
            common = self.twoPrefix(common, A[i])
    
        return common
