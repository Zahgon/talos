def parallel_gpu_jobs(allow_growth=True, fraction=.5):

    '''Sets the max used memory as a fraction for tensorflow
    backend

    allow_growth :: True of False

    fraction :: a float value (e.g. 0.5 means 4gb out of 8gb)

    '''

    pass


def multi_gpu(model, gpus=None, cpu_merge=True, cpu_relocation=False):

    '''Takes as input the model, and returns a model
    based on the number of GPUs available on the machine
    or alternatively the 'gpus' user input.

    NOTE: this needs to be used before model.compile() in the
    model inputted to Scan in the form:

    from talos.utils.gpu_utils import multi_gpu
    model = multi_gpu(model)

    '''
    pass


def force_cpu():

    '''Force CPU on a GPU system
    '''

    pass
