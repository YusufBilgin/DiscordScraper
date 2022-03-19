from pick import pick


def choose_action():
    title = 'Please choose an action'
    options = [
        'Print my account infos',
        'Print my friends list',
        'Print my dm channels',
        'Print my servers',
        'Print messages from a spesific channel'
    ]
    option, index = pick(options, title)

    return index

def save_or_not():
    title = "Should i save the result?"
    options = [
        'yes',
        'no'
    ]
    option, index = pick(options, title)

    return index
