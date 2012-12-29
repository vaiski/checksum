# -*- coding: utf-8 -*-

'''
Modulo 97-10
~~~~~~~~~~~~

Used ie. in IBAN and RF reference number.
'''

from ..checksum import (
    ChecksumStrategy,
)


class Mod9710(ChecksumStrategy):
    '''
    Provides Modulo 97-10 checksum algorithm.
    '''

    name = 'mod9710'

    TRANSFORM = {
        'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15',
        'G': '16', 'H': '17', 'I': '18', 'J': '19', 'K': '20', 'L': '21',
        'M': '22', 'N': '23', 'O': '24', 'P': '25', 'Q': '26', 'R': '27',
        'S': '28', 'T': '29', 'U': '30', 'V': '31', 'W': '32', 'X': '33',
        'Y': '34', 'Z': '35'
    }

    def checksum(self, body):
        body = self._prepare(body)
        checksum = 0
        checksum = (98 - (int(body) * 100) % 97) % 97
        if checksum < 10:
            checksum = '0' + str(checksum)
        else:
            checksum = str(checksum)
        return checksum

    def is_valid(self, value, checksum=None):
        if checksum is not None:
            value = '%s%s' % (value, checksum)
        return int(self._prepare(value)) % 97 == 1

    def split(self, value):
        return (value[:-2], value[-2:])

    def _prepare(self, body):
        retval = []
        for char in body:
            if char in self.TRANSFORM:
                retval.append(self.TRANSFORM[char])
            else:
                retval.append(char)
        return ''.join(retval)
