import unittest
import task
import math


class TestCase(unittest.TestCase):
    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def testAreaFromRadius(self):
        expected = [math.pi * (x*x) for x in range(100)]
        for ii in range(100):
            self.assertEqual(expected[ii], task.areaFromRadius(ii))

    def testFirstLastElement(self):
        for ii in range(100):
            myList = [x for x in range(ii+1)]
            firstLast = task.firstLastElement(myList)
            self.assertEqual(firstLast[0], 0)
            self.assertEqual(firstLast[1], ii)


if __name__ == '__main__':
    unittest.main()
