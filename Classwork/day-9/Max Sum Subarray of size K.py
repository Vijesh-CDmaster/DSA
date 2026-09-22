class Solution:
    def maxSubarraySum(self, arr, k):
        window = sum(arr[:k])
        maxi = window

        for i in range(k, len(arr)):
            window = window - arr[i-k] + arr[i]
            maxi = max(maxi, window)

        return maxi