import requests
from urllib.parse import urlparse

from colorama import init
from termcolor import colored

# use Colorama to make Termcolor work on Windows too
init(autoreset=True)


class Sqli:
    def __init__(self, verbose):
        self._verbose = verbose

    def _insert_sqli_payloads(self, url):
        parser_url = urlparse(url)

        links = url.split("?")[0]
        querys = parser_url.query.split("&")

        domain = []

        payloads = ("'")

        try:
            for payload in payloads:
                links_payload = links + "?" + ("&".join(
                    [query + payload for query in querys]))

                domain.append(links_payload)
        except Exception as e:
            print(colored(
                f"[+] Failed to inject SQL payload into target {url}: {e.msg}",
                'red'))

        return domain

    def _check_error(self, response_text):
        error_list = [
            "mysql_fetch_array()", "You have an error in your SQL syntax",
            "MySQL Query fail.", "PostgreSQL ERROR", "Access Database Engine",
            "Microsoft Access Driver"
        ]

        for error in error_list:
            if error in response_text:
                return True

        return False

    def check_vull(self, url_clean, verbose=False):
        url_with_payload = self._insert_sqli_payloads(url_clean)

        for url in url_with_payload:
            try:
                response = requests.get(url=url)
            except requests.exceptions.HTTPError:
                continue
            except requests.exceptions.ConnectionError:
                continue
            except requests.exceptions.ReadTimeout:
                continue

            if self._check_error(response.text):
                print(colored(f"[SUCCESS] - {url}", "yellow"))

            if self._verbose:
                print(colored(f"[ERROR] - {url}", "red"))
