# -*- coding: utf-8 -*-

'''
Module provides and registers checksum strategy classes for the context class.
'''

from ..checksum import Checksum
from .luhn10 import Luhn10
from .fact137 import Fact137
from .mod9710 import Mod9710
from .mod31 import Mod31
from .verhoeff import Verhoeff
from .fact12 import Fact12

Checksum.register_strategy(Luhn10)
Checksum.register_strategy(Fact137)
Checksum.register_strategy(Mod9710)
Checksum.register_strategy(Mod31)
Checksum.register_strategy(Verhoeff)
Checksum.register_strategy(Fact12)
