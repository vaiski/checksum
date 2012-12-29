# -*- coding: utf-8 -*-

'''
Factor 137
~~~~~~~~~~

Used ie. in Finnish domestic creditor reference and Finnish ID card number.
'''


from ..checksum import (
    ChecksumStrategy,
)


class Fact137(ChecksumStrategy):
    '''
    Provides Factorial 137 checksum algorithm.
    '''

    name = 'fact137'

    def checksum(self, body):

        digits = self._prepare(body)
        weights = [7, 3, 1, ]
        checksum = 0

        for i, digit in enumerate(digits[::-1]):
            fact = weights[i % 3]
            checksum += digit * fact
        checksum = (0 if checksum % 10 == 0 else 10 - checksum % 10)
        return str(checksum)

    # def is_valid(self, value, checksum=None):
    #     body = value
    #     if checksum is None:
    #         (body, checksum) = self.split(value)
    #     return self.checksum(body) == checksum

    def split(self, value):
        return (value[:-1], value[-1])
