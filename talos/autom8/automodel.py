class AutoModel:

    def __init__(self, task, experiment_name, metric=None):

        '''

        Creates an input model for Scan(). Optimized for being used together
        with Params(). For example:

        p = talos.AutoParams().params
        model = talos.AutoModel(task='binary').model

        talos.Scan(x, y, p, model)

        NOTE: the parameter space from Params() is very large, so use limits
        in or reducers in Scan() accordingly.

        task : string or None
            If 'continuous' then mae is used for metric, if 'binary',
            'multiclass', or 'multilabel', f1score is used. Accuracy is always
            used.
        experiment_name | str | Must be same as in `Scan()`
        metric : None or list
            You can also input a list with one or more custom metrics or names
            of Keras or Talos metrics.
        '''

        pass

    def _set_metric(self):

        """Sets the metric for the model based on the experiment type
        or a list of metrics from user."""
        pass

    def _create_input_model(self, x_train, y_train, x_val, y_val, params):

        pass
