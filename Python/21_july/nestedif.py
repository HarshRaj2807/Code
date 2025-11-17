d = {'harshad' :'nikky', 'ashu':'ashifa'}
username = input('Enter Username : ')
if username in d:
    password = input('Enter Password : ')
    if password==d[username]:
        print('Login Succesfull')
    else:
        print('Invalid Password')
else:
    print('Invalid Username')