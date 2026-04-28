class Analyze:

    '''A suite of commands that are useful for analyzing the results
    of a completed scan, or during a scan.

    filename :: the name of the experiment log from Scan()'''

    def __init__(self, source=None):

        '''Takes as input a filename to the experiment
        log or the Scan object'''

        pass

    def high(self, metric):

        '''Returns the highest value for a given metric'''

        pass

    def rounds(self):

        '''Returns the number of rounds in the experiment'''

        pass

    def rounds2high(self, metric):

        '''Returns the number of rounds it took to get to the
        highest value for a given metric.'''

        pass

    def low(self, metric):

        '''Returns the minimum value for a given metric'''

        pass

    def correlate(self, metric, exclude):

        '''Returns a correlation table against a given metric. Drops
        all other metrics and correlates against hyperparameters only.

        metric | str | Column label for the metric to correlate with
        exclude | list | Column label/s to be excluded from the correlation

        NOTE: You should use `exclude` to avoid correlating with other metrics.

        '''

        pass

    def plot_line(self, metric):

        '''A line plot for a given metric where rounds is on x-axis

        NOTE: remember to invoke %matplotlib inline if in notebook

        metric | str | Column label for the metric to correlate with

        '''
        pass

    def plot_hist(self, metric, bins=10):

        '''A histogram for a given metric

        NOTE: remember to invoke %matplotlib inline if in notebook

        metric | str | Column label for the metric to correlate with
        bins | int | Number of bins to use in histogram

        '''
        pass

    def plot_corr(self, metric, exclude, color_grades=5):

        '''A heatmap with a single metric and hyperparameters.

        NOTE: remember to invoke %matplotlib inline if in notebook

        metric | str | Column label for the metric to correlate with
        exclude | list | Column label/s to be excluded from the correlation
        color_grades | int | Number of colors to use in heatmap

        '''

        pass

    def plot_regs(self, x, y):

        '''A regression plot with data on two axis

        x = data for the x axis
        y = data for the y axis
        '''

        pass

    def plot_box(self, x, y, hue=None):

        '''A box plot with data on two axis

        x = data for the x axis
        y = data for the y axis
        hue = data for the hue separation
        '''
        pass

    def plot_bars(self, x, y, hue, col):

        '''A comparison plot with 4 axis'''
        pass

    def plot_kde(self, x, y=None):

        '''Kernel Destiny Estimation type histogram with
        support for 1 or 2 axis of data'''

        pass

    def table(self, metric, exclude=[], sort_by=None, ascending=False):

        '''Shows a table with hyperparameters and a given metric

        EXAMPLE USE:

        ra1 = Reporting('diabetes_1.csv')
        ra1.table(sort_by='fmeasure_acc', ascending=False)

        PARAMS:

        metric | str or list | Column labels for the metric to correlate with
        exclude | list | Column label/s to be excluded from the correlation
        sort_by | str | The colunm name sorting should be based on
        ascending | bool | Set to True when `sort_by` is to be minimized eg. loss

        '''

        pass

    def best_params(self, metric, exclude, n=10, ascending=False):

        '''Get the best parameters of the experiment based on a metric.
        Returns a numpy array with the values in a format that can be used
        with the talos backend in Scan(). Adds an index as the last column.

        metric | str or list | Column labels for the metric to correlate with
        exclude | list | Column label/s to be excluded from the correlation
        n | int | Number of hyperparameter permutations to be returned
        ascending | bool | Set to True when `metric` is to be minimized eg. loss

        '''

        pass

    def _cols(self, metric, exclude):

        '''Helper to remove other than desired metric from data table'''

        pass
