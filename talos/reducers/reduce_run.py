def reduce_run(self):

    '''The process run script for reduce
    procedures; takes care of everything
    related with reduction. When new
    reduction methods are added, they need
    to be added as options here.

    To add new reducers, create a file in /reducers
    which is where this file is located. In that file,
    take as input self from Scan() and give as output
    either False, which does nothing, or a tuple of
    'value' and 'label' where value is a parameter
    value and label is parameter name. For example
    batch_size and 128. Then add a reference to
    reduce_run.py and make sure that you process
    the self.param_object.param_index there before
    wrapping up.

    '''
    pass
