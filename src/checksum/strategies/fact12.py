# -*- coding: utf-8 -*-

'''
Factor 12
~~~~~~~~~~
'''

from ..checksum import (
    ChecksumStrategy,
)


class Fact12(ChecksumStrategy):
    '''
    Provides Factorial 12 checksum algorithm.
    '''

    name = 'fact12'

    def checksum(self, body):
        digits = self._prepare(body)
        checksum = 0

        odds = digits[-1::-2]
        evens = digits[-2::-2]
        checksum += sum(evens)
        checksum += sum(odds) * 2

        return str(checksum % 10)

    def split(self, value):
        return (value[:-1], value[-1])
