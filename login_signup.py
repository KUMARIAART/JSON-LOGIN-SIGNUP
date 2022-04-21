import json
print("WELCOME TO LOGIN SIGNUP PAGE:-")

option=input("what you want login and signup for login press 1 and for signup press 2:-")
if option=="1":
    out_file=open("login_signup.json","r")
    r=out_file.read()
    userdetail=json.loads(r)

    username=input("enter username:-")
    for i in userdetail:
        if username in userdetail[i]["name"]:
            print("username is already exist")
            print("TRY AGAIN")
            break
    password=input("enter your paasword")
    if len(password)==8:
        if ("#" in password or "$"in password or "@"in password or "-"in password or "&"in password):
            if ("0"in password or "1"in password or "2"in password or "3"in password or "4"in password or "5"in password or "6"in password or "7"in password or "8"in password or "9"in password):
                print("strong password")
                confirmpswrd=input("enter o``nce more a password for confiormation:-")
                if password==confirmpswrd:
                    phone_number=int(input("enter your phone number:-"))
                    date_of_birth=(input("enter your date of birth:-"))
                    gender=input("enter your gender:-")
                    print("YOUR ACCOUNT IS SUCCESSFULLY CREATED")
                else:
                    print("check password again")    
            else:
                print("atleast enter the number")
        else:
            print("atleast enter the special character")
    else:
        print("len of password is 8")
    userdetail[username]={"name":username,"password":password,"phone number":phone_number,"date of birth":date_of_birth,"gender":gender}
    out_file=open("login_signup.json","w")
    json.dump(userdetail,out_file,indent=5)

if option=="2":

    out_file=open("login_signup.json","r")
    r=out_file.read()
    userdetail=json.loads(r)

    username=input("enter username:-")
    password=input("enter your password:-")
        
    for i in userdetail:
        if username in userdetail[i]["name"]:
            if password in userdetail[i]["password"]:
                print("--------------YOUR ACCOUNT IS SUCESSFULLY LOGIN-------------")
                break
            else:
                print("password is wrong")  
        else:
            print("your userdtail is in valid first signup in page")
                


            
            

    
    



    

