import numpy as np
from tensorflow.keras.optimizers.legacy import Adam, Adagrad, SGD


loss = {'binary': ['binary_crossentropy', 'LogCosh'],
        'multi_class': ['sparse_categorical_crossentropy'],
        'multi_label': ['categorical_crossentropy'],
        'continuous': ['mae']}

last_activation = {'binary': ['sigmoid'],
                   'multi_class': ['softmax'],
                   'multi_label': ['softmax'],
                   'continuous': [None]}


class AutoParams:

    def __init__(self,
                 params=None,
                 task='binary',
                 replace=True,
                 auto=True,
                 network=True,
                 resample_params=4):

        '''A facility for generating or appending params dictionary.

        params : dict or None
        task : str
             'binary', 'multi_class', 'multi_label', or 'continuous'
        replace : bool
             Replace current dictionary entries with new ones.
        auto : bool
             Automatically generate or append params dictionary with
             all available parameters.
        network : bool
             Adds several network architectures as parameters. This is to be
             used as an input together with KerasModel(). If False then only
             'dense' will be added.
        resample_params | int or False | The number of values per parameter
        '''

        pass

    def _automated(self, shapes='fixed'):

        '''Automatically generate a comprehensive
        parameter dict to be used in Scan()

        shapes : string
            Either 'fixed' or 'sloped'

        '''
        pass

    def shapes(self, shapes='auto'):

        '''Uses triangle, funnel, and brick shapes.'''

        pass

    def shapes_slope(self, min_slope=0, max_slope=.6, steps=.1):

        '''Uses a single decimal float for values below 0.5 to
        reduce the width of the following layer.'''

        pass

    def layers(self, min_layers=0, max_layers=6, steps=1):

        pass

    def dropout(self, min_dropout=0, max_dropout=.85, steps=0.1):

        pass

    def optimizers(self, optimizers='auto'):

        '''If `optimizers='auto'` then optimizers will be picked based on
        automatically. Otherwise input a list with one or
        more optimizers will be used.
        '''

        pass

    def activations(self, activations='auto'):

        '''If `activations='auto'` then activations will be picked based on
        automatically. Otherwise input a list with one or
        more activations will be used.
        '''

        pass

    def losses(self, losses='auto'):

        '''If `losses='auto'` then losses will be picked based on
        `AutoParam()` argument `task`. Otherwise input a list with one or
        more losses will be used.
        '''

        pass

    def neurons(self, min_neuron=8, max_neuron=None, steps=None):

        '''`max` and `steps` has to be either `None` or
        integer value at the same time.'''

        pass

    def batch_size(self, min_size=8, max_size=None, steps=None):

        '''`max_size` and `steps` has to be either `None` or
        integer value at the same time.'''

        pass

    def epochs(self, min_epochs=50, max_epochs=None, steps=None):

        '''`max_epochs` and `steps` has to be either `None` or
        integer value at the same time.'''

        pass

    def kernel_initializers(self, kernel_inits='auto'):

        '''
        kernel_inits | list | one or more kernel initializers
        '''

        pass

    def lr(self, learning_rates='auto'):

        '''If `learning_rates='auto'` then a very wide range of learning rates
        will be added. Otherwise a list with one or more learning rates
        is used.

        NOTE: talos.utils.lr_normalizer should be used if more than one optimizer
        is used in the experiment
        '''

        pass

    def networks(self, networks='auto'):

        '''If `network='auto'` then dense, simplernn, lstm, conv1d, and
        bidirectional_lstm are added. Otherwise a list with one or more
        network architectures is used.
        '''

        pass

    def last_activations(self, last_activations='auto'):

        '''If `last_activations='auto'` then activations will be picked
        automatically based on `AutoParams` property `task`.
        Otherwise input a list with one or more activations will be used.
        '''

        pass

    def resample_params(self, n):

        '''Resamples params dictionary so that `n` values are present for each
        parameter.'''

        pass

    def _append_params(self, label, values):

        pass
