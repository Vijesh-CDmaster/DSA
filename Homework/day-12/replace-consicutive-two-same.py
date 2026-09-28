class Solution:
    def removeDuplicates(self, s):
        # code here
        ans = ""

        for i in range(len(s)):
            if i == 0 or s[i] != s[i - 1]:
                ans += s[i]

        return ans

