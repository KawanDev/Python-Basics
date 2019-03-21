# Python 3 make sure to make text file and rename whatever you want then change "data_1" to your variable name.
with open("password.txt", "r+") as f:
  data_1 = f.read() #Stores the content of the textfile
  f.seek(0) #Goes to the first "position" in the textfile
  username = input('What is your username?: ')
  password = input('What is your password?: ')
  f.write(data_1 + '\n' + 'Username: ' + username + '||' + 'Password: ' + password) #data_1(file) + new line for each
  print("Sucessfully wrote to file")
