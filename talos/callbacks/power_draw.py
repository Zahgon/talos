from tensorflow.keras.callbacks import Callback


class PowerDraw(Callback):

    '''A callback for recording GPU power draw (watts) on epoch begin and end.

    Example use:

    power_draw = PowerDraw()

    model.fit(...callbacks=[power_draw]...)

    history = talos.utils.power_draw_append(history, power_draw)

    '''

    def __init__(self):

        pass

    def on_train_begin(self, logs={}):
        pass

    def on_epoch_begin(self, batch, logs=None):
        pass

    def on_epoch_end(self, batch, logs=None):
        pass
