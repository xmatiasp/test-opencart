import unittest

from tests import testSignIn, testAddToCart

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(testSignIn))
suite.addTests(loader.loadTestsFromModule(testAddToCart))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)