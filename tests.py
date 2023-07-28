import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    def test1(self):
        """Verify that passwords less than 8 characters are rejected"""
        self.assertFalse(check_pwd('abcdabc'))

if __name__ == '__main__':
    unittest.main()
