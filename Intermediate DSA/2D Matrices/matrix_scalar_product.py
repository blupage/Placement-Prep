# You are given a matrix A and and an integer B, you have to perform scalar multiplication of matrix A with an integer B.

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] = A[i][j] * B
        return A