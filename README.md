# LeetCode Solutions By HansZhong
## Description
This Repository is created to record my algorithm exercising experiences on LeetCode.
### 1310. 子数组异或查询 \[[题目](https://leetcode-cn.com/problems/xor-queries-of-a-subarray/)]\[[题解](./Solutions/1310.py)]
解题思路：
* 异或运算具有如下性质：`x^x=0`、`x^0=x`
* 借用上述性质，可以得出数组下标i到下标j的元素的异或结果可以表达为前i-1个元素的异或结果和前j个元素的异或结果再取异或，即：`x[i]^...^x[j]=(x[0]^...^x[i-1])^(x[0]^...^x[i-1])^x[i]^...^x[j]=(x[0]^...^x[i-1])^(x[0]^...^x[j])=X[i]^X[j+1]`①，`X[n]=x[0]^...^X[n-1]`记为前缀异或和
* 综上，算法流程为：
	1. 一次遍历数组arr，计算前缀和X[n]并记录
	2. 一次遍历数组queries，利用①式计算结果并返回
