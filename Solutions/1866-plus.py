class Solution(object):
    def rearrangeSticks(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        NUM = [[0 for i in range(k)] for j in range(n)]
        mod = 10**9+7
        for i in range(n):
            for j in range(k):
                if(j==i):
                    NUM[i][j] = 1
                elif(j>i):
                    NUM[i][j] = 0
                elif(j==0):
                    NUM[i][j] = i*NUM[i-1][j] % mod
                else:
                    NUM[i][j] = (NUM[i-1][j-1] + i*NUM[i-1][j]) % mod
        return NUM[n-1][k-1]
