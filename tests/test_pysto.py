import unittest
from pysto import __version__


class TestPysto(unittest.TestCase):
    def test_version(self):
        self.assertEqual(__version__, "0.1.0")
