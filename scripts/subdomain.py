# Import required modules
import requests
from urllib.parse import urlparse

def subdomain(url, verbose):
    # Read words from wordlist
    wordlist = open("wordlists/subdomain-regular.txt", "r")
    urldata = urlparse(url)

    
    for word in wordlist:
        
        if urldata.netloc[:4] == "www.":
            url = "{}://{}.{}".format(urldata.scheme, word.rstrip(), urldata.netloc[4:])
        else:
            url = "{}://{}.{}".format(urldata.scheme, word.rstrip(), urldata.netloc)

        # Make request to the subdomain + url 
        # HAS ISSUES
        request = requests.get(url)
        print(request.status_code)
        # If verbose is True then print all results
        if verbose == True:
            print("["+str(request.status_code)+"] " + url)

        # If not verbose then only print results which are not 404
        elif request.status_code != 404:
            print("["+str(request.status_code)+"] " + url)
    