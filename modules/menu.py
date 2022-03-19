from colorama import Fore, init

init()


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
            Fore.CYAN + 'Options:' + Fore.RESET,
            calc_space(len('Options:'), 1, 39) + '#',
            Fore.CYAN + '[1]' + Fore.RESET,
            'Choose actions',
            Fore.CYAN + '[2]' + Fore.RESET,
            'Info'
        )
    )
