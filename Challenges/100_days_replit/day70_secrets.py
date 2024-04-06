import os

admin_password = os.environ['ADMIN_PASSWORD']
user_password = os.environ['USER_PASSWORD']


username = str(input('Username > '))
password = str(input('Password > '))

if username.lower()=='user' and password==user_password:
  print('Welcome User!!')
elif username.lower()=='admin' and password==admin_password:
  print('Welcome Admin!!')
else:
  print('username and password not macth!')