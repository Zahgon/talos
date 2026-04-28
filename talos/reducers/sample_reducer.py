def sample_reducer(limit, max_value, random_method):

    '''Sample Reducer (Helper)

    NOTE: The Scan() object  is in self.main_self because
    the object being passed here is ParamGrid() object where
    the Scan() object is attached as self.main_self.

    Utilize 'grid_downsample', 'shuffle', and 'random_method'
    to reduce the param_grid before starting the experiment.
    This is the simplest method in Talos for dealing with curse
    of dimensionality.

    Options are uniform random, stratified random, latin hypercube
    sampling, and latin hypercube with sudoku style constraint.

    Returns the reduced param_grid as numpy array.

    '''
    pass
