import os
from dotenv import load_dotenv


from question import questions

name = input("what youur name? ")

print("welcome")

score = 0

load_dotenv()
anmin_password = os.getenv("QYIZE_ADMIN_PASSWORD")
open_admin = input("do u want to open adnine mode? yes/no: ")
if open_admin.lower() == "yes":
    enter_password = input("enter admin password")

    if enter_password == anmin_password:
        print("admin! hi...")

    else:
        print("wrong password")



for item in questions :
    answer = input(item["question"])

    if answer.lower() == item["answer"]:
        print("correct")
        score += 1
    else:
        print("wrong")


print("your score is: ", score, "out of", len(questions))

if score == len(questions):
    print("exelent job", name)

elif score >= 2:
    print("god job", name)

else:
    print("keep practicing", name)


file = open("results.txt", "a")
file.write(f"{name} - {score}/{len(questions)}\n ")

file.close()