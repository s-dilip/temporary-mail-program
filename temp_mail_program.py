

import requests

def delete_user(user_id, jwt_token):

    endpoint_url = f"https://api.mail.tm/accounts/{user_id}"
    auth_headers = {"Authorization":f"Bearer {jwt_token}"}

    response = requests.delete(endpoint_url, headers=auth_headers)

    return response.text

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

    #print(retrieve_token('titan225@karenkey.com', 'pass123'))

    print(delete_user('636538d5fc7a242b9506e611', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2Njc1Nzg5NzMsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJ1c2VybmFtZSI6InRpdGFuMjI1QGthcmVua2V5LmNvbSIsImlkIjoiNjM2NTM4ZDVmYzdhMjQyYjk1MDZlNjExIiwibWVyY3VyZSI6eyJzdWJzY3JpYmUiOlsiL2FjY291bnRzLzYzNjUzOGQ1ZmM3YTI0MmI5NTA2ZTYxMSJdfX0.ant2Yc4Pv_WPI9pf-KGadgvLkVuQpNoWw1pFOZlSQXeyCIxry49a2QAQRSz5sge9mf44OThijZPGQpkCTsLEnw'))



main()

