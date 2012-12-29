# -*- coding: utf-8 -*-

import unittest
from ..checksum import Checksum


class Mod9710Test(unittest.TestCase):

    def setUp(self):
        self.cs = Checksum('mod9710')

    def tearDown(self):
        self.cs = None
        del self.cs

    def test_checksum_chars(self):
        ''' Calculate a checksum for body containing letters. '''

        self.cs.body = 'C2H5OHRF'
        self.assertEquals(self.cs.checksum(), '00')  # '97')

    def test_sanity(self):
        body = '0600001234567'
        self.cs.body = body
        checksum = self.cs.checksum()
        self.assertEquals(checksum, '58')
        self.assertEquals(self.cs.body, body)
        whole = '%s%s' % (self.cs.body, checksum)
        self.assertTrue(self.cs.is_valid(whole))

    def test_checksum_iban(self):
        ''' Calculate a checksum for a belgian and finnish example IBANs. '''

        self.cs.body = '510007547061BE'
        self.assertEquals(self.cs.checksum(), '62')

        self.cs.body = '068999999501BE'
        self.assertEquals(self.cs.checksum(), '43')

        self.cs.body = '15903000000776FI'
        self.assertEquals(self.cs.checksum(), '37')

    def test_validation_separate(self):
        self.assertTrue(self.cs.is_valid('567812F48K012', '54'))

    def test_validation_chars(self):
        self.assertTrue(self.cs.is_valid('422820512RF56'))

    def test_checksum_zero(self):
        self.cs.body = '97001'
        self.assertTrue(self.cs.checksum(), '01')

    # def test_zero_checksum(self):
    #     ''' Calculate a checksum for a body with a checksum of zero. '''

    #     self.cs.body = '3060599'
    #     self.assertEquals(self.cs.checksum(), '0')
