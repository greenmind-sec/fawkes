import requests
import random
import sys

from core.errors import GoogleError
from colorama import init
from termcolor import colored

# use Colorama to make Termcolor work on Windows too
init(autoreset=True)


class GoogleSearch:
    def __init__(self, params={}, timeout=1):
        self.params = params
        self.timeout = timeout
        self._malicious_traffic = "Our systems have detected unusual traffic"

    def _load_user_random_agents(self):
        with open("commonlist/user_agents.txt", "r") as user_agent:
            user_agents = user_agent.read().splitlines()
            user_agent = random.choice(list(user_agents))

        return user_agent

    def _load_random_google_url(self):
        with open("commonlist/google_url.txt", "r") as google_url:
            google_urls = google_url.read().splitlines()
            google_url = random.choice(list(google_urls))

        return google_url

    def request(self):
        google_url = self._load_random_google_url()
        user_agent = self._load_user_random_agents()

        print(colored(f"Random google URL: {google_url}", "green"))
        print(colored(f"Random User-Agent: {user_agent}", "green"))

        try:
            req = requests.get(
                url=google_url,
                params=self.params,
                timeout=self.timeout,
                headers={
                    "User-Agent": user_agent
                })

        except requests.exceptions.RequestException as e:
            print(f"[+] Requests error: {e}")
            sys.exit(1)

        if self._malicious_traffic in req.text:
            raise GoogleError("Google detected malicious traffic")

        return req
