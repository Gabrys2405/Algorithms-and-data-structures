
import unittest
from matrix import Matrix
import chio


class test_chio(unittest.TestCase):
    def test_1(self):
        mat = Matrix([[1,2,3,4,5],[2,5,8,1,4],[3,1,4,5,6],[2,3,4,6,8],[2,3,4,5,6]])
        det = chio.chio(mat)
        self.assertEqual(det, 50)


    def test_2(self):
        mat = Matrix([[0,2,3],[2,5,8],[3,1,4]])
        det = chio.chio(mat)
        self.assertEqual(det, -7)

    
    def test_3(self):
        mat = Matrix([[0,2,3,4,5],[2,5,8,1,4],[3,1,4,5,6],[2,3,4,6,8],[2,3,4,5,6]])
        det = chio.chio(mat)
        self.assertEqual(det, 130)


    def test_4(self):
        mat = Matrix([[0,2],[2,5]])
        det = chio.chio(mat)
        self.assertEqual(det, -4)

    
    def test_5(self):
        mat = Matrix([[1,2],[2,5]])
        det = chio.chio(mat)
        self.assertEqual(det, 1)