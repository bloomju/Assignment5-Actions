import unittest
import task
import math
import random
from datetime import date


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

    def testNumDays(self):
        dateL1 = [date(random.randrange(0, 10000), random.randrange(1, 13), random.randrange(1, 29)) for x in range(100)]
        dateL2 = [date(random.randrange(0, 10000), random.randrange(1, 13), random.randrange(1, 29)) for x in range(100)]
        expected = [abs((dateL1[x]-dateL2[x]).days) for x in range(100)]
        for ii in range(100):
            self.assertEqual(expected[ii], task.numDays(dateL1[ii], dateL2[ii]))


if __name__ == '__main__':
    unittest.main()
