import os
import platform


def command(command):
    print(f"Command : {command}")
    os.system(command)


def git_init():
    command("git init")


def git_add():
    command("git add file.txt")


def git_commit(date):
    command(f'git commit -m "hehehe I am chogosu" --date "{date} day ago"')


def git_push():
    command(f"git push -f origin main")


def delete_dotgit():
    if platform.system() == "Windows":
        command("rmdir /s /q .git")
    else:
        command("rm -rf .git")

def git_config(username, useremail, usertoken, repoaddr):
    command(f"git config --local user.name {username}")
    command(f"git config --local user.email {useremail}")
    command(f"git config --local user.password {usertoken}")
    command(f"git config --local credential.helper cache")
    command(f"git remote add origin {repoaddr}")