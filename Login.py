import getpass
users = { 'neko': 'buu',
          'ken' : 'gaki',
          'zell': 'perfect'
}
attempt = 3
while attempt > 0:
    
    username = input(" Enter username: ")
    password = getpass.getpass(" Enter password: ")
    
    if username in users and users[username]== password:
        print(f" Access granted, welcome {username} !")
        break
   
    else:
        attempt -= 1
        print(f" Access denied, you have {attempt} attempts left. ")
else:
    print(" Credentials could not be verified. ")

            
    
