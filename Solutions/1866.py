class Solution(object):
    def rearrangeSticks(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        NUM = [[0 for col in range(k)] for row in range(n)]

        NUM[0][0] = 1
        NUM[1][0] = 1

        mod = 10**9 + 7

        for i in range(2,n):
            NUM[i][0] = NUM[i-1][0] * i

        for i in range(1,k): #k
            for j in range(i,n-k+i+1): #n
                for p in range(i,j+1): #i
                    NUM[j][i] = NUM[j][i] + NUM[p-1][i-1] * (NUM[j][0] / NUM[p][0])
                    NUM[j][i] = NUM[j][i] % mod

        return NUM[n-1][k-1]
