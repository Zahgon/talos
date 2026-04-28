import inspect

import numpy as np
import itertools as it
from datetime import datetime


class ParamSpace:

    def __init__(self,
                 params,
                 param_keys,
                 random_method='uniform_mersenne',
                 fraction_limit=None,
                 round_limit=None,
                 time_limit=None,
                 boolean_limit=None):

        pass

    def _param_input_conversion(self):

        '''Parameters may be input as lists of single or
        multiple values (discrete values) or tuples
        (range of values). This helper checks the format of
        each input and handles it accordingly.'''
        pass

    def _param_apply_limits(self):

        pass

    def _param_range_expansion(self, param_values):

        '''Expands a range (tuple) input into discrete
        values. Helper for _param_input_conversion.
        Expects to have a input as (start, end, steps).
        '''
        pass

    def _param_space_creation(self):

        '''Expand params dictionary to permutations

        Takes the input params dictionary and expands it to
        actual parameter permutations for the experiment.
        '''
        pass

    def _check_time_limit(self):

        pass

    def round_parameters(self):

        # permutations remain in index
        pass

    def _round_parameters_todict(self, values):

        pass

    def _convert_lambda(self, fn):

        '''Converts a lambda function into a format
        where parameter labels are changed to the column
        indexes in parameter space.'''
        pass

    def remove_is_not(self, label, value):

        '''Removes baesd on exact match but reversed'''
        pass

    def remove_is(self, label, value):

        '''Removes based on exact match'''
        pass

    def remove_ge(self, label, value):

        '''Removes based on greater-or-equal'''
        pass

    def remove_le(self, label, value):

        '''Removes based on lesser-or-equal'''
        pass

    def remove_lambda(self, function):

        '''Removes based on a lambda function'''
        pass
