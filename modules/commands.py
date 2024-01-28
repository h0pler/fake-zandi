import os


def command(command):
    print(f"Command : {command}")
    os.system(command)


def git_init():
    if os.path.isdir(".git"):
        return 1
    else:
        command("git init")
        return 0


def git_add():
    command("git add file.txt")


def git_commit(date):
    command(f'git commit -m "hehehe I am chogosu" --date "{date} day ago"')


def git_push(branchname):
    command(f"git push -f origin {branchname}")
