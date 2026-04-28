from tensorflow.keras.callbacks import Callback


class ExperimentLog(Callback):

    def __init__(self,
                 experiment_name,
                 params):

        '''Takes as input the name of the experiment which will be
        used for creating a .log file with the outputs and the params
        dictionary from the input model in `Scan()`

        experiment_name | str | must match the experiment_name in `Scan()`
        params | dict | the params dictionary from the input model in `Scan()

        '''

        pass

    def on_train_begin(self, logs={}):

        pass

    def on_train_end(self, logs={}):

        pass

    def on_epoch_begin(self, epoch, logs={}):

        pass

    def on_epoch_end(self, epoch, logs={}):

        pass
