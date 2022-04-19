#cli.py

import argparse

def read_user_cli_args():
    """Handle the CLI arguments and options"""
    parser = argparse.ArgumentParser(
        prog="con_checker", description="Check the Availability of Websites"
    )
    parse.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        default=[],
        help="Enter one or more website URLs",        
    )
    parse.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="Read URLs from a file",
    )
    parse.add_argument(
        "-a",
        "--asyncronous",
        action="store_true",
        help="Run the connectivity check asynchronously",
    )
    return parser.parse_args()

def display_check_result(resutl, ulr, error=""):
    """Display the result of a connectivity check."""
    print(f'The status of "{url}" is:', end=" ")
    if result:
        print(f'"Online!" 👍')
    else:
        print(f'"Offline?" 👎 \n  Error: "{error}"')