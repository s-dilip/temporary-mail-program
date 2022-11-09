import time
import requests
import random

def delete_user(user_id, jwt_token):

    endpoint_url = f"https://api.mail.tm/accounts/{user_id}"
    auth_headers = {"Authorization":f"Bearer {jwt_token}"}

    response = requests.delete(endpoint_url, headers=auth_headers)

    return response

def retrieve_emails(jwt_token):

    endpoint_url = "https://api.mail.tm/messages"
    auth_headers = {"Authorization":f"Bearer {jwt_token}"}

    response = requests.get(endpoint_url, headers=auth_headers)
    json = response.json()

    return json['hydra:member']


def retrieve_token(email, password):

    endpoint_url = "https://api.mail.tm/token"
    post_body = {'address': email, 'password':password}

    response = requests.post(endpoint_url, json = post_body)
    json = response.json()

    print(json)

    return json['token']

def generate_rand_email():
    a = 1

def generate_user(domain, password):

    endpoint_url = "https://api.mail.tm/accounts"
    random_user_name= 'Hary' + str(random.randrange(1,999)) #Having 'Hary' is VERY IMPORTANT

    post_body = {'address': f'{random_user_name}@{domain}', 'password':f'{password}'}

    response = requests.post(endpoint_url, json=post_body)
    json = response.json()

    return json

def retrieve_domain():

    response = requests.get("https://api.mail.tm/domains")
    json = response.json()

    domain = json['hydra:member'][0]['domain']

    return domain

def main():

    try:
        print('Hello')

        password = 'pass123'

        domain = retrieve_domain()
        user_data = generate_user(domain, password)
        print(user_data)
        email_address = user_data['address']
        
        user_id = user_data['id']

        jwt_token = retrieve_token(email_address, password)
        
        print(f'You email Address is: {email_address}')
        print('Retrieving emails...')

        while 1:

            messages = retrieve_emails(jwt_token)

            for message in messages:

                sender_name = message['from']['name']
                sender_email = message['from']['address']

                print(f'Sent From: {sender_name}')
                print(f'Their Email: {sender_email}')

                print(f"{message['subject']}")
                print(f"{message['intro']}")

            
            time.sleep(5)

    except KeyboardInterrupt:

        print(delete_user(user_id, jwt_token))
        print('Keyboard Interrupt')

main()

