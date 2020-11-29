from core.filter import Filter
from engines.google import GoogleSearch
from vulls.sqli import Sqli

from colorama import init
from termcolor import colored
from multiprocessing.dummy import Pool as ThreadPool

# use Colorama to make Termcolor work on Windows too
init(autoreset=True)


class Scan(Filter):
    def __init__(self, args):
        self.args = args

    def _get_response(self):
        params = {
            'q': self.args.query,
            'start': self.args.start_page,
            'num': self.args.results
        }

        req = GoogleSearch(params=params, timeout=self.args.timeout)
        response = req.request()

        return response

    def scan(self):
        response = self._get_response()
        links = Filter(response).filter_links()
        links_parsed = self.remove_links(links)

        print(colored(f"Number of targets: {len(links_parsed)}", 'green'))
        print(colored("-" * 79, "grey"))

        sqli = Sqli(self.args.verbose)
        pool = ThreadPool(self.args.threads)

        pool_exec = pool.map(sqli.check_vull, links_parsed)
        pool.close()
        pool.join()
