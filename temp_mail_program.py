

import requests

def retrieve_token(email, password):

    endpoint_url = "https://api.mail.tm/token"
    post_body = {'address': email, 'password':password}

    response = requests.post(endpoint_url, json = post_body)
    json = response.json()

    return json['token']

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

    # domain = retrieve_domain()
    # post_response = generate_user(domain)
    # user_id = post_response['id'] #Use this when deleting the User

    # print(f"Your Email ID is: f{post_response['address']}")

    # print(domain)
    # print(post_response)

    print(retrieve_token('titan225@karenkey.com', 'pass123'))



main()

