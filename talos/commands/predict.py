class Predict:

    '''Class for making predictions on the models that are stored
    in the Scan() object'''

    def __init__(self, scan_object):

        '''Takes in as input a Scan() object and returns and object
        with properties for `predict` and `predict_classes`'''

        pass

    def predict(self,
                x,
                metric,
                asc,
                model_id=None,
                saved=False,
                custom_objects=None):

        '''Makes a probability prediction from input x. If model_id
        is not given, then best_model will be used.

        x | array | data to be used for the predictions
        model_id | int | the id of the model from the Scan() object
        metric | str | the metric to be used for picking best model
        asc | bool | True if `metric` is something to be minimized
        saved | bool | if a model saved on local machine should be used
        custom_objects | dict | if the model has a custom object,
                                pass it here

        '''

        pass

    def predict_classes(self,
                        x,
                        metric,
                        asc,
                        task,
                        model_id=None,
                        saved=False,
                        custom_objects=None):

        '''Makes a class prediction from input x. If model_id
        is not given, then best_model will be used.

        x | array | data to be used for the predictions
        model_id | int | the id of the model from the Scan() object
        metric | str | the metric to be used for picking best model
        asc | bool | True if `metric` is something to be minimized
        task | string | 'binary' or 'multi_label'
        saved | bool | if a model saved on local machine should be used
        custom_objects | dict | if the model has a custom object, pass it here
        '''

        pass
