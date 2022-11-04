

import requests

def generate_rand_email():
    a = 1

def generate_user(domain):

    endpoint_url = "https://api.mail.tm/accounts"

    post_body = {'address': f'titan225@{domain}', 'password':'pass123'}

    response = requests.post(endpoint_url, json=post_body)
    json = response.json()

    return json

def retrieve_domain():

    response = requests.get("https://api.mail.tm/domains")
    json = response.json()

    domain = json['hydra:member'][0]['domain']

    return domain

def main():

    domain = retrieve_domain()
    post_response = generate_user(domain)

    print(domain)
    print(post_response)

main()

