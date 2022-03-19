from colorama import Fore, Back, Style

def calc_space(string_length, before_length, max_length):
    a = int(max_length) - (int(before_length) + int(string_length))
    space = a * " "

    return str(space)

def menu():
    print("""
    #########################################
    #                                       #
    #      Welcome to Discord Scraper       #
    #                                       #
    # {}{}
    #  {}  {}                  #
    #  {}  {}                            #
    #                                       #
    #########################################
    """.format(
            Fore.CYAN + 'Options:' + Style.RESET_ALL,
            calc_space(len('Options:'), 1, 39) + '#',
            Fore.CYAN + '[1]' + Style.RESET_ALL,
            'Choose actions',
            Fore.CYAN + '[2]' + Style.RESET_ALL,
            'Info'
        )
    )
