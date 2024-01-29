import requests
import os
from dotenv import load_dotenv

load_dotenv()
github_token = os.getenv("GITHUB_TOKEN")


def get_username_from_token():
    url = "https://api.github.com/user"
    headers = {"Authorization": f"token {github_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("login")
    else:
        return None


def get_useremail_from_token():
    url = "https://api.github.com/user/emails"
    headers = {"Authorization": f"token {github_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        emails = response.json()
        for email in emails:
            if email["primary"]:
                return email["email"]
        return None
    else:
        return None

