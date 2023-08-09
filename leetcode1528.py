class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        def res():
            for i in sorted(indices):
                yield s[indices.index(i)]
        return ''.join(res())

a = Solution()
print(a.restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
print(a.restoreString(s = "abc", indices = [0,1,2]))