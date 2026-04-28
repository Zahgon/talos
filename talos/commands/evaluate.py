class Evaluate:

    '''Class for evaluating models based on the Scan() object'''

    def __init__(self, scan_object):

        '''Takes in as input a Scan() object.
        e = evaluate(scan_object) and see docstring
        for e() for more information.'''

        pass

    def evaluate(self,
                 x,
                 y,
                 task,
                 metric,
                 model_id=None,
                 folds=5,
                 shuffle=True,
                 asc=False,
                 saved=False,
                 custom_objects=None,
                 multi_input=False,
                 print_out=False):

        '''Evaluate a model based on f1_score (all except regression)
        or mae (for regression). Supports 'binary', 'multi_class',
        'multi_label', and 'regression' evaluation.

        x | array | The input data for making predictions
        y | array | The ground truth for x
        model_id | int | It's possible to evaluate a specific model based
                         on ID.
        folds | int | Number of folds to use for cross-validation
        sort_metric | string | A column name referring to the metric that
                               was used in the scan_object as a performance
                               metric. This is used for sorting the results
                               to pick for evaluation.
        shuffle | bool | Data is shuffled before evaluation.
        task | string | 'binary', 'multi_class', 'multi_label', or
                        'continuous'.
        asc | bool | False if the metric is to be optimized upwards
                     (e.g. accuracy or f1_score)
        saved | bool | if a model saved on local machine should be used
        custom_objects | dict | if the model has a custom object, pass it here
        multi_input | bool | if multi-input model is evaluated, set to True
        print_out | bool | Print out the results.

        TODO: add possibility to input custom metrics.

        '''
        pass
