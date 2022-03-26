import functools
from .cli.cli_forms import save_or_not
from .file_operations import save_content_to_txt

def template_decorator(func):
    '''This is a template for my decoraters'''

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before function
        func(*args, **kwargs)
        # Do something after function
        return None 
    return wrapper


def save_to_txt(func):
    '''Ask user if he wants to save the result to a .txt file'''

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before function
        if save_or_not() == 0:
            save = True
        else:
            save = False

        output = func(*args, **kwargs)

        # Do something after function
        if save == True:
            save_content_to_txt(output)
        return None 
    return wrapper
