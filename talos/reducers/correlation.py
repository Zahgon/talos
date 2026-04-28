def correlation(self, method):

    '''This is called from reduce_run.py.

    Performs a spearman rank order correlation
    based reduction. First looks for a parameter
    that correlates with reduction_metric and
    correlation meets reduction_threshold and
    then converts the match parameter into
    a 2d multilabel shape. Then new correlation
    against reduction_metric is performed to identify
    which particular value is to be dropped.

    '''
    pass
