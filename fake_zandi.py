import os
import commands as cmd

cnt = 0
file = "file.txt" 

def print_desc():
    print("*" * 10+"manual"+"*" * 10)
    print("1. git init")
    print("2. git remote add origin your_repo_addr")
    print("3. fake_zandi")
    
if not os.path.isfile(file):    
    open("file.txt","w")

print_desc()

while True:
    choice = int(input())
    if choice == 1:
        cmd.git_init()
    elif choice == 2:
        your_repo_addr = input("Input your repo addr :")
        cmd.command(f"git remote add origin {your_repo_addr}")
    elif choice == 3:
        day = input("since [?] days ago ... ")
        while cnt <= int(day):
            file = open("file.txt", "a")
            file.write("%d\n" % (cnt))
            cmd.git_init()
            cmd.git_add()
            cmd.git_commit(cnt)
            cnt += 1
        cmd.git_push()
        break
    else:
        print("Not found :(")