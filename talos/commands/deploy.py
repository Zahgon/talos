class Deploy:

    '''Functionality for deploying a model to a filename'''

    def __init__(self,
                 scan_object,
                 model_name,
                 metric,
                 asc=False,
                 saved=False,
                 custom_objects=None):

        '''Deploy a model to be used later or in a different system.

        NOTE: for a metric that is to be minimized, set asc=True or otherwise
        you will end up with the model that has the highest loss.

        Deploy() takes in the object from Scan() and creates a package locally
        that can be later activated with Restore().

        scan_object | object | The object that is returned from Scan() upon
                               completion.
        model_name | str | Name for the .zip file to be created.
        metric | str | The metric to be used for picking the best model.
        asc | bool | Make this True for metrics that are to be minimized
                     (e.g. loss), and False when the metric is to be
                     maximized (e.g. acc).
        saved | bool | if a model saved on local machine should be used
        custom_objects | dict | if the model has a custom object, pass it here

        '''

        pass

    def save_model_as(self):

        '''Model Saver
        WHAT: Saves a trained model so it can be loaded later
        for predictions by predictor().
        '''
        pass

    def save_details(self):

        pass

    def save_data(self):

        pass

    def save_results(self):

        pass

    def save_params(self):

        pass

    def save_readme(self):

        pass

    def package(self):

        pass
