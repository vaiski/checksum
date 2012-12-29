# -*- coding: utf-8 -*-

'''
Modulo 31
~~~~~~~~~

Used ie. Finnish SSN and Finnish property code.
'''

from ..checksum import (
    ChecksumStrategy,
)


class Mod31(ChecksumStrategy):
    '''
    Provides Modulo 31 checksum algorithm.
    '''

    name = 'mod31'

    _check = {
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'H', 17: 'J',
        18: 'K', 19: 'L', 20: 'M', 21: 'N', 22: 'P', 23: 'R', 24: 'S', 25: 'T',
        26: 'U', 27: 'V', 28: 'W', 29: 'X', 30: 'Y'
    }

    def checksum(self, body):
        checksum = 0
        checksum = int(body) % 31
        if checksum > 9:
            return self._check[checksum]
        return str(checksum)

    def split(self, value):
        return (value[:-1], value[-1])
