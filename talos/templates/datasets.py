def telco_churn(quantile=.5):

    '''Returns dataset in format x, [y1, y2]. This dataset
    is useful for demonstrating multi-output model or for
    experimenting with reduction strategy creation.

    The data is from hyperparameter optimization experiment with
    Kaggle telco churn dataset.

    x: features
    y1: val_loss
    y2: val_f1score

    quantile is for transforming the otherwise continuous y variables into
    labels so that higher value is stronger. If set to 0 then original
    continuous will be returned.'''

    pass


def icu_mortality(samples=None):

    pass


def titanic():

    pass


def iris():

    pass


def cervical_cancer():

    pass


def breast_cancer():

    pass


def mnist():

    '''Note that this dataset, unlike other Talos datasets,returns:

    x_train, y_train, x_val, y_val'''

    pass
