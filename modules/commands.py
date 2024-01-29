import os
import platform


def command(command):
    print(f"Command : {command}")
    os.system(command)


def git_init():
    if os.path.isdir(".git"):
        return 1
    else:
        command("git init")
        command("git branch -M main")
        return 0


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
