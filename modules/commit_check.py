import requests
import datetime
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


def check_commit_dates(n, username):
    today = datetime.date.today()
    commit_dates = []

    def get_github_events(page=1):
        url = f"https://api.github.com/users/{username}/events?page={page}"
        headers = {"Authorization": f"token {github_token}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    page = 1
    while True:
        events = get_github_events(page)
        if not events:
            break

        for event in events:
            if event["type"] == "PushEvent":
                commit_date = datetime.datetime.strptime(
                    event["created_at"], "%Y-%m-%dT%H:%M:%SZ"
                ).date()
                if commit_date >= today - datetime.timedelta(days=n):
                    commit_dates.append(commit_date)
                else:
                    missing_days = [
                        (today - date).days
                        for date in (
                            today - datetime.timedelta(days=i) for i in range(n)
                        )
                        if date not in commit_dates
                    ]
                    return missing_days

        page += 1

    missing_days = [
        (today - date).days
        for date in (today - datetime.timedelta(days=i) for i in range(n))
        if date not in commit_dates
    ]
    return missing_days
