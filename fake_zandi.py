import os
import commands as cmd

cnt = 0
file = "file.txt" 

def print_desc():
    print("*" * 10+"manual"+"*" * 10)
    print("1. remove existing .git folder")
    print("2. git init")
    print("3. your repo ? ")
    print("4. your branch ? ")
    print("5. let's go !!")
    
if not os.path.isfile(file):    
    open("file.txt","w")

while True:
    print_desc()
    choice = int(input())
    if choice == 1:
        cmd.command("rm -rf .git")
    elif choice == 2:
        cmd.git_init()
    elif choice == 3:
        your_repo_addr = input("Input your repo addr :")
        cmd.command(f"git remote add origin {your_repo_addr}")
    elif choice == 4:
        your_branch_name = input("Input your branch name :")
        cmd.command(f"git checkout -b {your_branch_name}")
    elif choice == 5:
        day = input("since [?] days ago ... ")
        while cnt <= int(day):
            file = open("file.txt", "a")
            file.write("%d\n" % (cnt))
            cmd.git_add()
            cmd.git_commit(cnt)
            cnt += 1
        cmd.git_push(your_branch_name)
        break
    else:
        print("Not found :(")