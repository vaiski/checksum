# -*- coding: utf-8 -*-

import unittest

from .fact12_test import Fact12Test
from .fact137_test import Fact137Test
from .luhn10_test import Luhn10Test
from .mod31_test import Mod31Test
from .mod9710_test import Mod9710Test
from .verhoeff_test import VerhoeffTest


def test_all():
    '''
    Creates a test suite for running all the tests.
    '''

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Fact12Test))
    suite.addTest(unittest.makeSuite(Fact137Test))
    suite.addTest(unittest.makeSuite(Luhn10Test))
    suite.addTest(unittest.makeSuite(Mod31Test))
    suite.addTest(unittest.makeSuite(Mod9710Test))
    suite.addTest(unittest.makeSuite(VerhoeffTest))
    return suite
