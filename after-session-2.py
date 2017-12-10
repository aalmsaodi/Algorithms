#Linked Lists: Swap List Nodes in pairs ************************************
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        counter = 0
        tempValue = A.val
        currentNode = A
        
        while currentNode.next != None:
            
            if counter%2 == 0:
                tempValue = currentNode.val
                currentNode.val = currentNode.next.val
            else:
                currentNode.val = tempValue
            
            currentNode = currentNode.next
            counter += 1
        
        if counter%2 != 0:
            currentNode.val = tempValue
        
        return A
#Linked Lists: Add Two Numbers as Lists ************************************
class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        carryOver = 0
        resArray = []
        
        currentA = A
        currentB = B
        while(currentA != None and currentB != None):
            resArray.append((carryOver + currentA.val + currentB.val)%10)
            carryOver = (carryOver + currentA.val + currentB.val)/10
            
            currentA = currentA.next
            currentB = currentB.next
        
        while(currentA != None):
            resArray.append((carryOver + currentA.val)%10)
            carryOver = (carryOver + currentA.val)/10
            currentA = currentA.next
            
        while(currentB != None):
            resArray.append((carryOver + currentB.val)%10)
            carryOver = (carryOver + currentB.val)/10
            currentB = currentB.next
            
        if carryOver != 0:
            resArray.append(carryOver)
            
        
        map(str, resArray)
        resArray = list(reversed(resArray))
        headList = ListNode(resArray.pop())
        current = headList
        
        while len(resArray) != 0:
            temp = ListNode(resArray.pop())
            current.next = temp
            current = temp
            
        return headList

#Hashing: Longest Substring Without Repeat ************************************
class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        longestSub = 0
        tempDict = dict()
        tempStartIndex = 0
        tempCurrentIndex = 0
        
        for i in xrange(len(A)):
          if A[i] not in tempDict or tempDict[A[i]] < tempStartIndex:
            tempDict[A[i]] = i
          else:
            repeatedCharIndex = tempDict[A[i]]
            currentLength = i - tempStartIndex
            longestSub = max(longestSub, currentLength)
            tempStartIndex = repeatedCharIndex + 1
            tempDict[A[i]] = i
            
        return max(len(A) - tempStartIndex, longestSub)
    
#Hashing: 2 Sum ************************************
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        hashMap = dict()
        possibleSolutions = []
        lowestIndex2 = 9999999
        lowestIndex1 = 9999999
        
        for i in xrange(len(A)):
            if str(A[i]) not in hashMap.keys():
                hashMap[str(A[i])] = i
        
        for i in xrange(len(A)):
            remaining = B - A[i]
            if str(remaining) in hashMap.keys():
                index1 = min(i, hashMap[str(remaining)])
                index2 = max(i, hashMap[str(remaining)])
                possibleSolutions.append([index1, index2])
        
        for solution in possibleSolutions:
            if solution[1] < lowestIndex2 and solution[0] < solution[1]:
                    lowestIndex2 = solution[1]
                    lowestIndex1 = solution[0]
        
        if possibleSolutions != []:
            return [lowestIndex1+1, lowestIndex2+1]
        else:
            return []
