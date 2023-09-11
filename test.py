class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mylist=[]
        longeststr=0
        for i in s:
            mylist.append(i)
        for i in range(len(s)):
            j=i+1
            if j is len(s):
                j=len(s)-1
            print(mylist[i],mylist[j])
            if mylist[i]!=mylist[j]:
                longeststr+=1
            else:
                longeststr+=1
        print(longeststr)
a=Solution()
a.lengthOfLongestSubstring("ab")