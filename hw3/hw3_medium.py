import numpy as np


class InitClass:
    def __init__(self):
        self.arr = None


class GetMixin(InitClass):

    def getArr(self):
        return self.arr


class SetMixin(InitClass):
    def setArr(self, value):
        self.arr = value


class StrMixin(InitClass):

    def __str__(self):
        return '[' + '\n '.join([str(i) for i in self.arr]) + ']'


class FilePrintMixin(InitClass):
    def filePrint(self, file):
        with open(file, 'w') as f:
            f.write(self.__str__())


class Matrix(np.lib.mixins.NDArrayOperatorsMixin, GetMixin, SetMixin, StrMixin, FilePrintMixin):
    def __init__(self, arr):
        super().__init__()
        self.arr = np.asarray(arr)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        inputs = tuple(x.arr for x in inputs)
        return getattr(ufunc, method)(*inputs, **kwargs)


if __name__ == "__main__":
    np.random.seed(0)

    m1 = Matrix(np.random.randint(0, 10, (10, 10)))
    m2 = Matrix(np.random.randint(0, 10, (10, 10)))

    matSum = Matrix(m1 + m2)
    matProd = Matrix(m1 * m2)
    matMatMul = Matrix(m1 @ m2)
    matSum.filePrint("artifacts/medium/matrix+.txt")
    matProd.filePrint("artifacts/medium/matrix*.txt")
    matMatMul.filePrint("artifacts/medium/matrix@.txt")
