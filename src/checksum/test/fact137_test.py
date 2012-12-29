# -*- coding: utf-8 -*-


import unittest
from .. import Checksum

BODY = '617435'
CHECKSUM = '4'
WHOLE = BODY + str(CHECKSUM)


class Fact137Test(unittest.TestCase):
    def setUp(self):
        self.cs = Checksum('fact137')

    def tearDown(self):
        del self.cs

    def test_checksum(self):
        ''' Calculate fact137 checksum for body. '''

        self.cs.body = BODY
        self.assertEquals(self.cs.checksum(), CHECKSUM)

    def test_zero_checksum(self):
        ''' Calculate fact137 checksum for a body with checksum of zero. '''

        self.cs.body = '59073839'
        self.assertEquals(self.cs.checksum(), '0')

    def test_splitting(self):
        ''' Split the input string correctly into body and checksum. '''

        self.assertEquals(self.cs.split(WHOLE), (BODY, CHECKSUM))

    def test_validation(self):
        self.assertTrue(self.cs.is_valid('503227814'))
        self.assertTrue(self.cs.is_valid('1234561'))
        self.assertTrue(self.cs.is_valid('590738390'),
                        'validation with a zero as checksum')

    def test_type(self):
        ''' Provide correct strategy name. '''

        self.assertEquals(self.cs.type(), 'fact137')
