# -*- coding: utf-8 -*-

'''
Checksum
========

Provides an extendable checksum calculation and validation library for
different checksum algorithms.
'''


class ChecksumStrategy(object):
    '''
    An interface class for checksum algorithm classes.
    '''

    def checksum(self, body):
        ''' Calculates a checksum for the body string provided. '''

        raise NotImplementedError('Checksum calculation is not implemented for'
                                  'this checksum strategy.')

    def is_valid(self, value, checksum=None):
        '''
        Validates a string against the checksum.

        This abstract base class provides an elementary checksum validation
        method. Advanced validation methods should be implemented in
        subclasses when possible.
        '''

        body = value
        if checksum is None:
            (body, checksum) = self.split(value)
        return self.checksum(body) == checksum

    def split(self, value):
        '''
        Splits the string including a checksum according to the checksum
        algorithm used.
        '''

        raise NotImplementedError('Splitting is not implemented for this '
                                  'checksum strategy.')

    def _prepare(self, body):
        ''' Method to prepare the body string for checksum calculation. '''

        return [int(d) for d in str(body)]


class Checksum(object):

    '''
    Checksum context class. Provides different checksum calculation and
    verification algorithms by acting as a factory class.
    '''

    _strategies = {}

    def __init__(self, strategy=None, body=None):
        '''
        Checksum context class constructor.
        :param strategy : name of the used checksum algorithm
        :param body : string that the checksum is calculated for
        '''

        self._strategy = None
        self._body = None
        self.strategy = strategy
        self.body = body

    # Setters and getters
    # -------------------

    @property
    def body(self):
        ''' Getter for the body property. '''
        return self._body

    @body.setter
    def body(self, value):
        ''' Setter for the body property. '''
        if value is not None:
            self._body = value
        else:
            self._body = ''

    @property
    def strategy(self):
        ''' Getter for the strategy property. '''
        return self._strategy

    @strategy.setter
    def strategy(self, value):
        ''' Setter for the strategy property. '''
        if value is None:
            return
        if value in self._strategies:
            strategy = self._strategies[value]()
        else:
            raise NotImplementedError('Checksum strategy %s is not '
                                      'implemented.' % value)

        if (isinstance(strategy, ChecksumStrategy) and
                type(strategy) != ChecksumStrategy):
            self._strategy = strategy
        else:
            raise TypeError(
                'Strategy requires a subclass of ChecksumStrategy.'
                ' Got instead %s.' % type(strategy))

    def checksum(self):
        '''
        Calculates the checksum using selected algorithm for the body string.
        '''
        if self.strategy is not None:
            return self.strategy.checksum(self._body)

    def is_valid(self, value, checksum=None):
        '''
        Validates either a string containing a checksum or a body string and
        a against separately provided checksum.
        '''
        if self.strategy is not None:
            return self.strategy.is_valid(value, checksum)

    def split(self, value):
        '''
        Splits a string containing a body and a checksum according to the
        conventions of selected checksum algorithm.
        '''
        if self.strategy is not None:
            return self.strategy.split(value)

    def type(self):
        '''
        Returns the name of used checksum algorithm.
        '''

        if self.strategy is not None:
            return self.strategy.name
        else:
            return None

    @classmethod
    def register_strategy(cls, strategy_cls):
        '''
        Registers a checksum strategy class in the available checksum
        strategies.
        '''

        strategy = strategy_cls()
        if (isinstance(strategy, ChecksumStrategy) and
                type(strategy) != ChecksumStrategy):
            cls._strategies[strategy_cls.name] = strategy_cls
        else:
            raise TypeError(
                'Strategy requires a subclass of ChecksumStrategy.'
                ' Got instead %s.' % type(strategy))

    @classmethod
    def list_strategies(cls):
        '''
        Lists all the available strategies for checksum calculation.
        '''

        return cls._strategies.keys()
