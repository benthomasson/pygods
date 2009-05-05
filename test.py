#!/usr/bin/env python

import unittest
import pygods
from coroutine import coroutine


class SimTest(pygods.SimObject):
    @coroutine
    def foo(self):
        while True:
            x = yield
            print x

class TestYield(unittest.TestCase):

    def testObject(self):
        sim = pygods.SimObject()
        sim.run()

    def testSim(self):
        sim = SimTest()
        sim.target = sim.foo()
        sim.run()



if __name__ == '__main__':
    unittest.main()

