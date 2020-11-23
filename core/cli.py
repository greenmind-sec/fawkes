import argparse


help_msg='''
    -e, --engine     - Specifies the search engine to be used.
    -q, --query      - Dork that will be used in the search engine.
    -r, --results    - Number of results brought by the search engine.
    -s, --start-page - Home page of search results.
    -t, --timeout    - Timeout of requests.
    -v, --verbose    - Enable verbosity.

Examples:
    fawkes --engine google --query 'noticias.php?id=10' --timeout 3 --verbose
    fawkes --engine google --query 'admin.php?id=1' --timeout 3 --verbose
'''


class Cli:
    def cli_parser(self):
        parser = argparse.ArgumentParser(add_help=False, usage=help_msg)

        parser.add_argument('-e',
                            '--engine',
                            required=True)

        parser.add_argument('-q',
                            '--query',
                            required=True)

        parser.add_argument('-r',
                            '--results',
                            type=int,
                            default=100,
                            required=False)

        parser.add_argument('-s',
                            '--start-page',
                            type=int,
                            default=0,
                            required=False)

        parser.add_argument('-t',
                            '--timeout',
                            type=int,
                            default=1,
                            required=False)

        parser.add_argument('-v',
                            '--verbose',
                            action="store_true",
                            required=False)

        return parser.parse_args()
