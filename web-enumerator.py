# Imoprt required modules
import argparse
import re
from scripts.directory import directory

# Create a function which checks if the given url is valid
def url_type(arg_value, pattern=re.compile("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")):

    # If the regex doesn't match, raise an error
    if not pattern.match(arg_value):
        raise argparse.ArgumentTypeError
    return arg_value

# Create the argument parser
parser = argparse.ArgumentParser(description="A simple program which enumerates web applications using a combination of custom and third-party scripts.")

# Create the arguments
parser.add_argument("-u", "--url", type=url_type, metavar="", help="url of the site to enumerate", required=True)
parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose mode", required=False)

# Parse the arguments
args = parser.parse_args()

directory(args.url, args.verbose)
