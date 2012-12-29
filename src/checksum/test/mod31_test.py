# -*- coding: utf-8 -*-

import unittest
from ..checksum import Checksum

CHECKDIGITS = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E',
    'F', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
    'Y'
]


class Mod31Test(unittest.TestCase):

    def setUp(self):
        self.cs = Checksum('mod31')

    def tearDown(self):
        self.cs = None
        del self.cs

    def test_checksum(self):
        ''' Calculate a checksum for body. '''

        self.cs.body = '131052308'
        self.assertEquals(self.cs.checksum(), 'T')

    def test_zero_checksum(self):
        ''' Calculate a checksum for a body with a checksum of zero. '''

        self.cs.body = '3060599'
        self.assertEquals(self.cs.checksum(), '0')

    def test_checksum_negative(self):
        '''
        Check digit does not match other possible (incorrect) check
        digits.
        '''

        self.cs.body = '123456'
        for c in CHECKDIGITS:
            if c is not 'E':
                self.assertNotEquals(self.cs.checksum(), c)
