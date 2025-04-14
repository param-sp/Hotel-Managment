import datetime
from datetime import date
meanu = {
    "poha" : 25,
    "upma" : 35,
    "shabu khichadi" : 50,
    "edli" : 30,
    "dhosa" : 80,
    "masala dhosa" : 110,
    "uttapa" : 90,
    "masala uttapa" :120,
    "onian uttapa" : 100,
    "hot cofee" : 30,
    "cold cofee" : 60,

}
print("*"*50)
print("Welcome To MODERN Resturant !!!")
print("\t MENUE \t\npoha = 25.Rs\nupma = 35.Rs\nshabu khichadi = 50.Rs\nedli = 30.Rs\ndhosa = 80.Rs\nmasala dhosa = 110.Rs\nuttapa = 90.Rs\nmasala uttapa = 120.Rs\nonian uttapa = 100.Rs\nhot cofee = 30.Rs\ncold cofee = 60.Rs")
print("*"*50)

item = input("Please... Enter A Product Which Want From Meanu : ").lower()
total_bill = 0
if item in meanu :
    print(f"Your {item} Has Been Ordered , Please Wait 10 minute To serve You !!!")
    total_bill += meanu[item]
else:
    print("Please Select From The Meanu !!!!!!")


while True:
    choise = input("Do You Want To Add Another Product (yes/no) :-  ").lower()
    if choise == "yes" :
        item = input("Please... Enter A Product Which Want From Meanu : ").lower()

        if item in meanu :
            print(f"Your {item} Has Been Ordered , Please Wait 10 minute To serve You !!!")
            total_bill += meanu[item]
        else:
            print("Please Select From The Meanu !!!!!!")
    else :
        print("Thank You To visiting .....")
        break

print(f"Your Total Bill Is {total_bill}.Rs")
print("Thank You For Visiting Modern Resturant.....")

with open("manage.txt","a") as file :
    file.writelines("===================================================\n")
    file.writelines("Welcome To MODERN Resturant !!!\n")
    file.writelines("\t MENUE \t\npoha = 25.Rs\nupma = 35.Rs\nshabu khichadi = 50.Rs\nedli = 30.Rs\ndhosa = 80.Rs\nmasala dhosa = 110.Rs\nuttapa = 90.Rs\nmasala uttapa = 120.Rs\nonian uttapa = 100.Rs\nhot cofee = 30.Rs\ncold cofee = 60.Rs\n")
    file.writelines("===================================================\n")
    file.writelines(f"Your Total Bill Is {total_bill}.Rs\n")
    file.writelines("Thank You For Visiting Modern Resturant.....\n")

with open("manage1.txt","w") as file :
    file.writelines("===================================================\n")
    file.writelines("Welcome To MODERN Resturant !!!\n")
    file.writelines("\t MENUE \t\npoha = 25.Rs\nupma = 35.Rs\nshabu khichadi = 50.Rs\nedli = 30.Rs\ndhosa = 80.Rs\nmasala dhosa = 110.Rs\nuttapa = 90.Rs\nmasala uttapa = 120.Rs\nonian uttapa = 100.Rs\nhot cofee = 30.Rs\ncold cofee = 60.Rs\n")
    file.writelines("===================================================\n")
    file.writelines(f"Your Total Bill Is {total_bill}.Rs\n")
    file.writelines("Thank You For Visiting Modern Resturant.....\n")

choise1 = input("Do You Want A Bill Recipet (yes/no) : ")
if choise1 == "yes":
    with open("manage1.txt","r") as file:
        new = file.read()
        print(new)
else :
    print("thank You")

command = "time"

if "time" in command:
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(now)
    today = date.today()
    new3 = today
    print(today)

with open("manage.txt","a") as file :
    file.writelines(f"{now}\n")
    file.writelines(f"{new3}\n")

with open("manage1.txt","w") as file :
    file.writelines(f"{now}\n")
    file.writelines(f"{new3}\n")