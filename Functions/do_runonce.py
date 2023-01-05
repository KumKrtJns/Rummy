def do_runonce(fun):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return fun(*args, **kwargs)

    wrapper.has_run = False
    return wrapper
