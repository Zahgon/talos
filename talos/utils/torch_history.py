class TorchHistory:

    '''This is a helper for replicating the history object
    behavior of Keras to make Talos Scan() API consistent between
    the two backends.'''

    def __init__(self):

        pass

    def init_history(self):
        pass

    def append_history(self, history_data, label):
        pass

    def append_loss(self, _loss):
        pass

    def append_metric(self, _metric):
        pass

    def append_val_loss(self, _loss):
        pass

    def append_val_metric(self, _loss):
        pass
