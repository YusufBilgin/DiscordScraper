import functools

def template_decorator(func):
    '''This is a template for my decoraters'''

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before function
        func(*args, **kwargs)
        # Do something after function
        return None 
    return wrapper
