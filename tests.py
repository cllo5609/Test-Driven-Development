# Author     : Clinton Lohr
# Date       : 02/17/2023
# Course     : CS 362 - Software Engineering II
# Assignment : TDD Hands On

from check_pwd import check_pwd
import unittest


class TestCase(unittest.TestCase):

    def test_01(self):
        input_str = ''
        self.assertFalse(check_pwd(input_str))

    def test_02(self):
        input_str = '1234567'
        self.assertFalse(check_pwd(input_str))

    def test_03(self):
        input_str = 'abcdefghijklmnopqrstu'
        self.assertFalse(check_pwd(input_str))


if __name__ == '__main__':
    unittest.main()
