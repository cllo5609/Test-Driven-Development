# Author     : Clinton Lohr
# Date       : 02/17/2023
# Course     : CS 362 - Software Engineering II
# Assignment : TDD Hands On

from check_pwd import check_pwd
import unittest


class TestCase(unittest.TestCase):

    # Verifies if an empty string returns False
    def test_01(self):
        input_str = ''
        self.assertFalse(check_pwd(input_str))

    # Verifies if a string of length less than 8 returns False
    def test_02(self):
        input_str = '1234567'
        self.assertFalse(check_pwd(input_str))

    # Verifies if a string of length greater than 20 returns False
    def test_03(self):
        input_str = 'abcdefghijklmnopqrstu'
        self.assertFalse(check_pwd(input_str))

    # Verifies if a string that does not contain at least one lowercase letter returns False
    def test_04(self):
        input_str = '123456789'
        self.assertFalse(check_pwd(input_str))

    # Verifies if a string that does not contain at least one uppercase letter returns False
    def test_05(self):
        input_str = '123435678u'
        self.assertFalse(check_pwd(input_str))

    # Verifies if a string that does not contain at least one digit returns False
    def test_06(self):
        input_str = 'aBcDeFgHi'
        self.assertFalse(check_pwd(input_str))

    # Verifies if a string that does not contain at least one special character returns False
    def test_07(self):
        input_str = '1234aBcD'
        self.assertFalse(check_pwd(input_str))


if __name__ == '__main__':
    unittest.main()
