from test import *
import unittest
import glob


if __name__ == "__main__":
    testsuite = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=1).run(testsuite)