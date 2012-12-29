# -*- coding: utf-8 -*-

import unittest
from ..checksum import Checksum


class Fact12Test(unittest.TestCase):

    def setUp(self):
        self.cs = Checksum('fact12')

    def test_checksum(self):
        ''' Calculate fact12 checksum for a body. '''

        self.cs.body = '1138574'
        self.assertEquals(self.cs.checksum(), '2')
