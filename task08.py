user = {
    'name': 'Ali',
    'email': 'aligmail.com'
}

if '@' not in user.values():
    user['email'] = 'ali@gmail.com'
    print(user)