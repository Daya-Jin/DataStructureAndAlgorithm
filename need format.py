class Solution:


    def findMode(self, root: 'TreeNode') -> 'List[int]':


    if not root:
    return []
a = self.bitree(root)
N = len(a)
maxfreq = 1
s = [a[0]]
freq = 1
for i in range(1, N):
    if a[i] == a[i - 1]:
    freq += 1
if freq == maxfreq:
    s.append(a[i])
elif freq > maxfreq:
s = [a[i]]
maxfreq = freq
else:
freq = 1
if maxfreq == 1:
    s.append(a[i])
return s


def bitree(self, root):


    if not root:
    return []
else:
if root.left:
    left = self.bitree(root.left)
else:
left = []
if root.right:
    right = self.bitree(root.right)
else:
right = []
return left + [root.val] + right
