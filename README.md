## Fawkes

<p align="center">
  <h3 align="center">Fawkes</h3>
  <p align="center">Fawles is a tool for Advanced search in search engines.</p>

  <p align="center">
    <a href="https://twitter.com/0xdutra">
      <img src="https://img.shields.io/badge/twitter-@0xdutra-blue.svg">
    </a>
    <a href="https://www.gnu.org/licenses/gpl-3.0">
      <img src="https://img.shields.io/badge/License-GPLv3-blue.svg">
    </a>
  </p>
</p>

<hr>

## Options

```
    -e, --engine     - Specifies the search engine to be used.
    -q, --query      - Dork that will be used in the search engine.
    -r, --results    - Number of results brought by the search engine.
    -s, --start-page - Home page of search results.
    -t, --timeout    - Timeout of requests.
    -v, --verbose    - Enable verbosity.

Examples:
    python3 fawkes.py --engine google --query 'noticias.php?id=10' --timeout 3 --verbose
    python3 fawkes.py --engine google --query 'admin.php?id=1' --timeout 3 --verbose
```
