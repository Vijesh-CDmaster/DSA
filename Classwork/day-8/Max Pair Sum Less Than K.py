class Solution:
    def maxSum(self, arr, k):
        arr.sort()

        left = 0
        right = len(arr) - 1

        max_sum = -1
        ans = (-1, -1)

        while left < right:
            s = arr[left] + arr[right]

            if s < k:
                if s > max_sum:
                    max_sum = s
                    ans = (arr[left], arr[right])

                elif s == max_sum:
                    if arr[right] - arr[left] > ans[1] - ans[0]:
                        ans = (arr[left], arr[right])

                left += 1

            else:
                right -= 1

        return ans