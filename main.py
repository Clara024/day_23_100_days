print ("LOGIN SYSTEM")
print("Welcome, Please fill in your username and password")

def login():
  while True:
#Get username and password from user
    username =input("What is your username?:")
    password =input("What is your password?:")
    if username == "Clara" and password =="bosslady":
      print("We have missed you. Welcome!")
      break
    else:
      print("Sorry, wrong username or password. Try again")
      print()

login()