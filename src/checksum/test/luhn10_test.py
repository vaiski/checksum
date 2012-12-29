# -*- coding: utf-8 -*-

import unittest
from .. import Checksum


BODY = '7992739871'
CHECKSUM = '3'
WHOLE = BODY + str(CHECKSUM)


class Luhn10Test(unittest.TestCase):
    def setUp(self):
        self.cs = Checksum('luhn')

    def tearDown(self):
        del self.cs

    def test_checksum(self):
        ''' Calculate luhn10 checksum for body. '''

        self.cs.body = BODY
        self.assertEquals(self.cs.checksum(), CHECKSUM)

    def test_splitting(self):
        ''' Split the input string correctly into body and checksum. '''

        self.assertEquals(self.cs.split(WHOLE), (BODY, CHECKSUM))

    def test_validation(self):
        ''' Validate a string with a correct checksum. '''

        self.assertTrue(self.cs.is_valid(WHOLE))
        self.assertTrue(self.cs.is_valid('12345600000785'),
                        "validate FKL's example BBAN")

    def test_type(self):
        ''' Provide correct strategy name. '''

        self.assertEquals(self.cs.type(), 'luhn')

    def test_negative_validation(self):
        for i in range(0, 9):
            if str(i) != CHECKSUM:
                self.assertFalse(self.cs.is_valid(BODY + str(i)),
                                 'validated %s as correct checksum for %s' %
                                 (i, BODY))
