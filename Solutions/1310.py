class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        arrxor = [0] * (len(arr)+1)
        for i in range(len(arr)):
            arrxor[i+1] = arr[i] ^ arrxor[i]
        xorqueries = [0] * len(queries)
        for i in range(len(queries)):
            xorqueries[i] = arrxor[queries[i][0]] ^ arrxor[queries[i][1]+1]
        return xorqueries
