def trees(self, quantile=.8):

    '''Extra Trees based reduction strategy. Like 'forrest', somewhat more
    aggressive than for example 'spearman' because there are no
    negative values, but instead the highest positive correlation
    is minused from all the values so that max value is 0, and then
    values are turned into positive. The one with the highest positive
    score in the end will be dropped. This means that anything with
    0 originally, is a candidate for dropping. Because there are multiple
    zeroes in many cases, there is an element of randomness on which one
    is dropped.

    '''
    pass
