import copy
import numpy as np


class Matrix:

    def __init__(self, a):
        self.arr = a

    def __add__(self, m):
        ans = copy.deepcopy(self.arr)
        for i in range(len(m.arr)):
            for j in range(len(m.arr[i])):
                ans[i][j] += m.arr[i][j]
        return Matrix(ans)

    def __mul__(self, m):
        ans = copy.deepcopy(self.arr)
        for i in range(len(m.arr)):
            for j in range(len(m.arr[i])):
                ans[i][j] *= m.arr[i][j]
        return Matrix(ans)

    def __matmul__(self, m):
        ans = [[0 for _ in range(len(m.arr[0]))] for _ in range(len(self.arr))]
        for i in range(len(self.arr)):
            for j in range(len(m.arr[0])):
                for k in range(len(m.arr)):
                    ans[i][j] += self.arr[i][k] * m.arr[k][j]
        return Matrix(ans)

    def filePrint(self, file):
        with open(file, 'w') as f:
            f.write(str(self.arr))


if __name__ == "__main__":
    np.random.seed(0)

    m1 = Matrix(np.random.randint(0, 10, (10, 10)))
    m2 = Matrix(np.random.randint(0, 10, (10, 10)))

    matSum = Matrix(m1 + m2)
    matProd = Matrix(m1 * m2)
    matMatMul = Matrix(m1 @ m2)

    matSum.filePrint("artifacts/easy/matrix+.txt")
    matProd.filePrint("artifacts/easy/matrix*.txt")
    matMatMul.filePrint("artifacts/easy/matrix@.txt")
