def recover_best_model(x_train,
                       y_train,
                       x_val,
                       y_val,
                       experiment_log,
                       input_model,
                       metric,
                       multi_input=False,
                       x_cross=None,
                       y_cross=None,
                       n_models=5,
                       task='multi_label'):

    '''Recover best models from Talos experiment log.

    x_train | array | same as was used in the experiment
    y_train | array | same as was used in the experiment
    x_val | array | same as was used in the experiment
    y_val | array | same as was used in the experiment
    experiment_log | str | path to the Talos experiment log
    input_model | function | model used in the experiment
    metric | str | use this metric to pick evaluation candidates
    multi_input | bool | set to True if multi-input model
    x_cross | array | data for the cross-validation or None for use x_val
    y_cross | array | data for the cross-validation or None for use y_val
    n_models | int | number of models to cross-validate
    task | str | binary, multi_class, multi_label or continuous

    Returns a pandas dataframe with the cross-validation results
    and the models.

    '''

    pass
