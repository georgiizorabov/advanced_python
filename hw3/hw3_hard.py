import numpy as np
from hw3_easy import Matrix


class HashMixin:
    def __hash__(self: Matrix):
        return int(sum([sum(el) for el in self.arr]))  # simply sum of all elements in matrix


class HashMatrix(Matrix, HashMixin):
    __hashed = dict()

    def __str__(self):
        return '[' + '\n '.join([str(i) for i in self.arr]) + ']'

    def __matmul__(self, m):
        hs = hash(self)
        hm = hash(m)

        if (hs, hm) in self.__hashed:
            return self.__hashed[(hs, hm)]
        ans = super().__matmul__(m)
        self.__hashed[(hs, hm)] = ans
        return ans


if __name__ == "__main__":
    np.random.seed(0)
    while True:
        A = HashMatrix(np.random.randint(0, 10, (3, 3)))
        B = HashMatrix(np.random.randint(0, 10, (3, 3)))
        C = HashMatrix(np.random.randint(0, 10, (3, 3)))
        D = B
        AB = A @ B
        CD = C @ D

        if (hash(A) == hash(C)) and (A != C) and (AB != CD):
            with open('artifacts/hard/A.txt', 'w') as f:
                f.write(A.__str__())
            with open('artifacts/hard/B.txt', 'w') as f:
                f.write(B.__str__())
            with open('artifacts/hard/C.txt', 'w') as f:
                f.write(C.__str__())
            with open('artifacts/hard/D.txt', 'w') as f:
                f.write(D.__str__())
            with open('artifacts/hard/AB.txt', 'w') as f:
                f.write(AB.__str__())
            with open('artifacts/hard/CD.txt', 'w') as f:
                f.write(CD.__str__())
            with open('artifacts/hard/hash.txt', 'w') as f:
                f.write(str(hash(AB)) + ' ' + str(hash(CD)))
            break
