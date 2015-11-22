while True:
    user = raw_input('plz input your name:')
    userlist = file('userlist.txt')
    while user in userlist.readline():
        while True:
            password = raw_input('plz input your password:')
            
