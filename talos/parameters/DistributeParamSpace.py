class DistributeParamSpace:

    def __init__(self,
                 params,
                 param_keys,
                 random_method='uniform_mersenne',
                 fraction_limit=None,
                 round_limit=None,
                 time_limit=None,
                 boolean_limit=None,
                 machines=2):

        '''Splits ParamSpace object based on number
        of machines.

        params | object | ParamSpace class object
        machines | int | number of machines to split for

        NOTE: `Scan()` limits will not be applied if ParamSpace object
        is passed directly into `Scan()` as `params` argument so they
        should be passed directly into `DistributeParamSpace` instead.

        '''

        pass

    def _split_param_space(self):

        '''Takes in a ParamSpace object and splits it so that
        it can be used in DistributeScan experiments.'''
        pass
