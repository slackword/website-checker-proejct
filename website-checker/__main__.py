#__main__.py

import pathlib
import sys

from website-checker.checker import site_is_online
from website-checker.cli import display_check_result, read_user_cli_args

def main():
    """Run Con_Checker."""
    user_args = read_user_cli_args()
    urls = _get_website_urls(user_args)
    if not urls:
        print(f'Error: no URLS to check', file=sys.stderr)
        sys.exit(1)
    _synchronous_check(urls)

def _get_website_urls(user_args):
    urls = user_args.urls
    if user_args.input_file:
        urls += _read_urls_from_file(user_args.input_file)
    return urls

def _read_urls_from_file(file):
    file_path = pathlib.Path(file)
    if file_path.is_file():
        with file_path.open() as urls_file:
            urls = [url.strip() for url in urls_file]
            if urls:
                return urls
            print(f"Error: empty input file, {file}", file=sys.stderr)
    else:
        print(f"Error: input file not found", file=sys.stderr)
    return[]

def _syncronous_check(urls):
    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)

if __name__ == "__main__":
    main()
