class AutoScan:

    def __init__(self,
                 task,
                 experiment_name,
                 max_param_values=None):

        '''Configure the `AutoScan()` experiment and then use
        the property `start` in the returned class object to start
        the actual experiment.

        `task` | str | 'binary', 'multi_class', 'multi_label', or 'continuous'
        `max_param_values` | int | Number of parameter values to be included.
                                   Note, this will only work when `params` is
                                   not passed as kwargs in `AutoScan.start`.
        '''

        pass

    def start(self, x, y, **kwargs):

        '''Start the scan. Note that you can use `Scan()` arguments as you
        would otherwise directly interacting with `Scan()`.

        `x` | array or list of arrays | prediction features
        `y` | array or list of arrays | prediction outcome variable
        `kwargs` | arguments | any `Scan()` argument can be passed here

        '''

        pass
