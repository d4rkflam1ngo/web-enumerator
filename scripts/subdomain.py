# Import required modules
import requests
from urllib.parse import urlparse

def subdomain(url, verbose):

    # Read words from wordlist
    wordlist = open("wordlists/subdomain-regular.txt", "r")

    # Parse the URL
    urldata = urlparse(url)

    
    for word in wordlist:
        
        # If the subdomain www. is present - remove it.
        if urldata.netloc[:4] == "www.":
            url = "{}://{}.{}".format(urldata.scheme, word.rstrip(), urldata.netloc[4:])

        else:

            # URL = scheme + subdomain + domain 
            url = "{}://{}.{}".format(urldata.scheme, word.rstrip(), urldata.netloc)

        # Make request to the subdomain + url 
        # HAS ISSUES
        request = requests.get(url)
        
        # If verbose is True then print all results
        if verbose == True:
            print("["+str(request.status_code)+"] " + url)

        # If not verbose then only print results which are not 400
        elif request.status_code != 400:
            print("["+str(request.status_code)+"] " + url)
    