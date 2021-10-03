# Imoprt required modules
import argparse
import re
from scripts.directory import directory
from scripts.subdomain import subdomain

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
parser.add_argument("-q", "--quick", action="store_true", help="quick scan mode", required=False)
parser.add_argument("-a", "--aggressive", action="store_true", help="aggressive/full scan mode", required=False)

# Parse the arguments
args = parser.parse_args()

directory(args.url, args.verbose)
subdomain(args.url, args.verbose)