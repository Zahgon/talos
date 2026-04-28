def epoch_entropy(self, history):

    '''Called from logging/logging_run.py

    Computes the entropy for epoch metric
    variation. If validation is on,
    then returns KL divergence instead of
    simple Shannon entropy. When Keras
    validation_freq is on, Shannon entropy
    is returned. Basically, all experiments
    should use validation, so Shannon is
    provided mearly as a fallback.

    '''
    pass
