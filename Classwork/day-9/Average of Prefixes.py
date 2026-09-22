class Solution:
    def prefixAvg(self, arr):
        total = 0
        ans = []

        for i in range(len(arr)):
            total += arr[i]
            ans.append(total // (i + 1))

        return ans