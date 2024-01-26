import os

cnt = 1
file = "file.txt"

def command(command):
    print(f"Command : {command}")
    os.system(command)
    
def clear():
    os.system("cls")

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
        command("git init")
        print("Create git init !!")
    elif choice == 2:
        your_repo_addr = input("Input your repo addr :")
        command(f"git remote add origin {your_repo_addr}")
        print("Success remote repo_addr")
    elif choice == 3:
        day = input("1 ~ day ago : ")
        while cnt <= int(day):
            file = open("file.txt", "a")
            file.write("%d\n" % (cnt))
            if not os.path.isfile(".git"):
                print(".git exist !!")
            else:
                print("Create git init")
                command("git init")
                clear()
            command("git add .")
            command(f"git commit -m \"fake_zandi\" --date \"{cnt} day ago\"")
            command("git push origin master")
            cnt += 1
    else:
        print("Not found :(")

file.close()