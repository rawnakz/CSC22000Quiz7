from typing import List

def findContentChildren(g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    i = j = count = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1
    return count

# Quick checks
print(findContentChildren([1,2,3], [1,1]))     # 1
print(findContentChildren([1,2], [1,2,3]))     # 2
