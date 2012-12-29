# -*- coding: utf-8 -*-

'''
Luhn modulo 10
~~~~~~~~~~~~~~

Used ie. in credit card numbers and Finnish BBAN.
'''

from ..checksum import (
    ChecksumStrategy,
)


class Luhn10(ChecksumStrategy):
    '''
    Provides Luhn modulo 10 checksum algorithm.
    '''

    name = 'luhn'

    def checksum(self, body):

        digits = self._prepare(body)
        odds = digits[-1::-2]
        evens = digits[-2::-2]
        checksum = 0
        checksum += sum(evens)

        for digit in odds:
            checksum += sum(self._prepare(digit * 2))

        checksum = 10 - int(str(checksum)[-1])
        return str(checksum)

    def split(self, value):
        return (value[:-1], value[-1])
