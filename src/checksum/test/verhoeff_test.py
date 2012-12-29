# -*- coding: utf-8 -*-

import unittest
from ..checksum import Checksum


class VerhoeffTest(unittest.TestCase):

    def setUp(self):
        self.cs = Checksum('verhoeff')

    def test_checksum(self):
        ''' Calculate Verhoeff checksum for a body. '''

        self.cs.body = '75872'
        self.assertEquals(self.cs.checksum(), '2')

    def test_validity(self):
        ''' Validate correctly a valid code. '''

        self.assertTrue(self.cs.is_valid('123451'))

    def test_validity_negative(self):
        ''' Detect invalidity of permuted code. '''

        self.assertFalse(self.cs.is_valid('132451'))
