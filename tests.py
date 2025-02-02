import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    def test1(self):
        """Verify that passwords less than 8 characters are rejected"""
        self.assertFalse(check_pwd('abcdabc'))
        
    def test2(self):
        """Verify that passwords greater than 20 characters are rejected"""
        self.assertFalse(check_pwd('abcdabcdabcdabcdabcda'))
        
    def test3(self):
        """Verify that password contains at least 1 lower case letter"""
        self.assertFalse(check_pwd('12345678'))
        
    def test4(self):
        """Verify that the password contains at least 1 upper case letter"""
        self.assertFalse(check_pwd('abcdabcd'))
        
    def test5(self):
        """Verify that the password contains at least 1 digit"""
        self.assertFalse(check_pwd('abcdABCD'))
        
    def test6(self):
        """Verify that the password contains one of the required special characters"""
        self.assertFalse(check_pwd('abcABC12'))

if __name__ == '__main__':
    unittest.main()
