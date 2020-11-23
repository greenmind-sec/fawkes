from colorama import init
from termcolor import colored


# use Colorama to make Termcolor work on Windows too
init(autoreset=True)


def banner():
    banner='''
███████╗ █████╗ ██╗    ██╗██╗  ██╗███████╗███████╗
██╔════╝██╔══██╗██║    ██║██║ ██╔╝██╔════╝██╔════╝
█████╗  ███████║██║ █╗ ██║█████╔╝ █████╗  ███████╗
██╔══╝  ██╔══██║██║███╗██║██╔═██╗ ██╔══╝  ╚════██║
██║     ██║  ██║╚███╔███╔╝██║  ██╗███████╗███████║
╚═╝     ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝

Author: @0xdutra
Version: 1.0.0
Bugs: https://github.com/0xdutra/fawkes/issues
---------------------------------------------------
    '''

    print(colored(banner, 'green'))
