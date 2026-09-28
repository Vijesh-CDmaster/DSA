class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = []

        for char in s:
            if char not in result:
                result.append(char)

        return "".join(result)