

import requests


def retrieve_domain():

    response = requests.get("https://api.mail.tm/domains")
    json = response.json()

    domain = json['hydra:member'][0]['domain']

    return domain

def main():

    domain = retrieve_domain()
    print(domain)

main()

