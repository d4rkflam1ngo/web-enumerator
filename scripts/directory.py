# Import required modules
import requests

def directory(url, verbose, quick, aggressive):

    # If quick mode is set, use quick wordlist
    if quick:
        wordlist = open("wordlists/directory-quick.txt", "r")

    #  TODO: If aggressive mode is set, use aggressive wordlist
    elif aggressive:
        wordlist = []

    # Else, use the regular wordlist
    else:
        wordlist = open("wordlists/directory-regular.txt", "r")

    # File extensions to check
    extensions = ["", ".txt", ".php", ".html", ".js"]

    for word in wordlist:
        for extension in extensions:

            # Make request to the url + directory + extension
            request = requests.get(url + "/" + word.strip() + extension)

            # If verbose is True then print all results
            if verbose == True:
                print("["+str(request.status_code)+"] " + url + "/" + word.strip() + extension)

            # If not verbose then only print results which are not 404
            elif request.status_code != 404:
                print("["+str(request.status_code)+"] " + url + "/" + word.strip() + extension)
    