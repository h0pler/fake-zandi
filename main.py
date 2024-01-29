import os
import modules.commands as cmd
import modules.usercheck as usercheck
import random

cnt = 0
file = "file.txt"
if not os.path.isfile(file):
    open("file.txt", "w")

username = usercheck.get_username_from_token()
useremail = usercheck.get_useremail_from_token()
usertoken=os.getenv("GITHUB_TOKEN")
repoaddr=os.getenv("REPO_ADDR")
print(f"username : {username}\nuseremail : {useremail}\nusertoken : {usertoken}\nrepoaddr : {repoaddr}")

if not username or not useremail or not usertoken or not repoaddr:
    print("Check the example.env file.")
    print("Set the environment variables.")
    exit(1)
else:
    cmd.delete_dotgit()
    cmd.git_init()
    cmd.git_config(username, useremail, usertoken, repoaddr)
    day = input("Check commits for the last [?] days ... :  ")
    # missing_days = usercheck.check_commit_dates(int(day), username)
    # for i in missing_days:
    #     randnum = random.randint(1, 5)
    #     for j in range(randnum):
    #         file = open("file.txt", "a")
    #         file.write("%d\n" % (i + j))
    #         cmd.git_add()
    #         cmd.git_commit(i)
    cmd.git_push()