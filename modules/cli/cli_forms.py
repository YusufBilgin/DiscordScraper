from pick import pick


def choose_action() -> int:
    title = 'Please choose an action'
    options = [
        'Print my account infos',
        'Print my friends list',
        'Print my dm channels',
        'Print my guilds',
        'Print messages from a spesific channel',
        'Print messages from a dm channel',
        'Print guild channels',
    ]
    option, index = pick(options, title)

    return index

def save_or_not() -> int:
    title = "Should i save the result?"
    options = [
        'yes',
        'no'
    ]
    option, index = pick(options, title)

    return index
