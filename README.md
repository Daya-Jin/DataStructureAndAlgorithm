# DataStructureAndAlgorithm
算法实现与刷题代码。文件夹计划分为两个：[BlankBoard](https://github.com/Daya-Jin/DataStructureAndAlgorithm/tree/master/BlankBoard)跟[OnlineExam](https://github.com/Daya-Jin/DataStructureAndAlgorithm/tree/master/OnlineExam)。前者要求是白板能徒手写出来的水平；而后者题意偏应用，主要针对在线笔试。

## 题目思路套路及总结

以下内容不分顺序。

### DFS

个人将DFS归为一种特殊的递归，大部分情况下DFS相当于暴力解，通过搜索问题的大部分子空间甚至所有子空间，根据根据符合题意的方向不断深入搜索。个人习惯使用的dfs函数有两个重要参数：```idx```与```path```，前者指示当前搜索的一个定位，后者表示从初始点到现在为止成功探索出来的路径。注意```path```不是```res```，但是可以看做是不完整的```res```，当满足条件时需要把```path```转成```res```或者加到```res```中去。

DFS在递归调用时通常使用线性访问的顺序来避免访问重复地点。

典型题目：[Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)。

### BFS

BFS作为DFS的兄弟，同样是通过搜索问题子空间来得到解，不过个人习惯使用队列来实现BFS而不是递归。

典型题目：[Friend Circles](https://leetcode.com/problems/friend-circles/)。

### Bit Option

题目中最常用的位操作不过于**与**、**异或**和**移位**三中操作。

**与**操作常用于提取某一位的数字，跟$1$相与相当于提取最低位，跟$2$相与相当于提取倒数第$2$位，跟$3$相与相当于提取低两位，以此类推。

**异或**操作常用来实现取反跟去重。跟$1$异或相当于取反，如$0\oplus{1}=1$、$1\oplus{1}=0$；去重的原理是因为任何数跟自身异或都等于$0$。
