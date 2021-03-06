# LeetCode Solutions By HansZhong
## Description
This Repository is created to record my algorithm exercising experiences on LeetCode.
### 1310. 子数组异或查询 \[[题目](https://leetcode-cn.com/problems/xor-queries-of-a-subarray/)]\[[题解](./Solutions/1310.py)]
解题思路：
* 异或运算具有如下性质：`x^x=0`、`x^0=x`
* 借用上述性质，可以得出数组下标i到下标j的元素的异或结果可以表达为前i-1个元素的异或结果和前j个元素的异或结果再取异或，即：`x[i]^...^x[j]=(x[0]^...^x[i-1])^(x[0]^...^x[i-1])^x[i]^...^x[j]=(x[0]^...^x[i-1])^(x[0]^...^x[j])=X[i]^X[j+1]`①，`X[n]=x[0]^...^X[n-1]`记为前缀异或和
* 综上，算法流程为：
	1. 一次遍历数组arr，计算前缀异或和X[n]并记录
	2. 一次遍历数组queries，利用①式计算结果并返回
* 类似的使用前缀和的想法在`积分图`中也有应用
* 算法复杂度为`O(n)`

### 1866. 恰有k根木棍可以看到的排列数目 \[[题目](https://leetcode-cn.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/)]\[[题解](./Solutions/1866.py)]\[[优化题解](./Solutions/1866-plus.py)]
解题思路：
* 本题是典型的动态规划问题，原因如下：最长的木棍一定可以看到，最长的木棍后面的木棍一定看不到。因此对于`(n,k)`问题（n根木棍中恰有k根木棍可以看到），最长的木棍共有`(n-k+1)`种放法（若最长的木棍放在小于k的位置则一定不满足`(n,k)`）若最长的木棍放在第i个位置，则最长的木棍前面的i-1根木棍构成子问题`(i-1,k-1)`，而最长的木棍后面的n-i根木棍共有`A(n-1,n-i)`种放法。故动态规划的递推式为：`NUM(n,k)=∑_i=k^n of [NUM(i-1,k-1) * A(n-1,n-i)]`
* 由于需要用到阶乘，且观察发现`NUM(i,1)`的值对应`(i-1)!`，可以重复利用减少计算量。
* 上述算法复杂度为`O(nk^2)`
- [x] 提交发现超时，需要进一步优化
* 分析最后一根木棍，共存在两种情况：其一，若最后一根木棍可以被看到，则它一定是当前所有可用木棍中最长的一根；其二，若最后一根木棍不能被看到，则它可能是除了当前所有可用木棍中最长的一根之外的任意一根木棍。故动态规划的递推式为：`NUM(n,k)=NUM(n-1,k-1)+(n-1)*NUM(n-1,k)`
* 注意：初始化条件为`NUM(1,1) = 1`，特别地，对于k=1，递推式为`NUM(n,k)=(n-1)*NUM(n-1,k)`，对于n=k，递推式为`NUM(k,k)=NUM(k-1,k-1)=...=NUM(1,1)=1`
* 上述算法复杂度为`O(nk)`
