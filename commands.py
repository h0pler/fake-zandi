import os

def command(command):
    print(f"Command : {command}")
    os.system(command)

def clear():
    os.system("cls")

def git_init():
    if not os.path.isfile(".git"):
        print(".git exist !!")
    else:
        print("Create git init")
        command("git init")
        clear()

def git_add():
    command("git add .")

def git_commit(date):
    command(f"git commit -m \"fake_zandi\" --date \"{date} day ago\"")

def git_push():
    command("git push origin master")
