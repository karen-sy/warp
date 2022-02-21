import unittest
import sys
import os
from unittest import runner

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests = unittest.TestSuite()
result = unittest.TestResult()

import warp as wp

import test_codegen
import test_mesh_query_aabb
import test_conditional
import test_operators
import test_rounding
import test_hash_grid
import test_ctypes
import test_rand
import test_noise
import test_tape
import test_compile_consts
import test_volume

tests.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_codegen))
tests.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_mesh_query_aabb))
tests.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_conditional))
tests.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_operators))
tests.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_rounding))
tests.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_hash_grid))
tests.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_ctypes))
tests.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_rand))
tests.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_noise))
tests.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_tape))
tests.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_compile_consts))
tests.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_volume))


# load all modules
wp.force_load()

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2, failfast=False)
    ret = not runner.run(tests).wasSuccessful()
    sys.exit(ret)
