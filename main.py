import os
import modules.commands as cmd
import modules.commit_check as commit_check
import random

cnt = 0
file = "file.txt"
if not os.path.isfile(file):
    open("file.txt", "w")

username = commit_check.get_username_from_token()
if not username:
    print("Check the example.env file")
    print("Set the GITHUB_TOKEN variable in the .env file.")
    exit(1)
else:
    print(f"Your username : {username}")
    if cmd.git_init() == 1:
        print("Already initialized. Please remove .git folder")
        exit(1)
    else:
        print("Initialized successfully")
        your_repo_addr = input("Input your repo addr :")
        cmd.command(f"git remote add origin {your_repo_addr}")
        your_branch_name = input("Input your branch name :")
        cmd.command(f"git checkout -b {your_branch_name}")
        day = input("Check commits for the last [?] days ... :  ")
        missing_days = commit_check.check_commit_dates(int(day), username)
        for i in missing_days:
            randnum = random.randint(1, 10)
            for j in range(randnum):
                file = open("file.txt", "a")
                file.write("%d\n" % (i))
                cmd.git_add()
                cmd.git_commit(i)
        cmd.git_push(your_branch_name)
