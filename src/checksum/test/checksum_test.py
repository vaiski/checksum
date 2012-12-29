# -*- coding: utf-8 -*-

import unittest
from ..checksum import Checksum


class ChecksumTest(unittest.TestCase):

    def setUp(self):
        self.cs = Checksum()

    def test_body_sanity(self):
        BODY_TEXT = '12345678'
        self.cs.body = BODY_TEXT
        self.assertEquals(self.cs.body, BODY_TEXT)
