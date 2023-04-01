ccode = ("1")
cpassword = ("1")

document = ("You Have not Created Any Documents\n\n")

restart = ("1")

if restart == ("1"):
  restart = ("0")
  
  password = input ('type the password\n')
  
  if password == (cpassword):
    print (" ")
    print ("Welcome Back!\n")
    print ("enter security code to access further info\n")
  
  code = input('type security code')

  if code == (ccode):
    print ( )
    print ("type d to enter diary")
    print ("")
    print ("press b to enter bank account")
    print ("")
    print ("press n to create new document")
    print ("")
    print ("press t to view your recent doc")
    print ("")
    print ("press e to edit your recent doc")
    print ("")
    print ("press c to change account info")
    print ("")
    print ("press r to restart")
    print ("")

  while cpassword == (cpassword):
  
    key = input('')
  
    if key == ("d"):
      print ("\nDear diary. I just talked with the manager of McDonalds after this brat got my order all wrong. People just don't understand.")

    if key == ("b"):
      print ("\nCurrent Blance: $45USD")

    if key == ("n"):
      document = input('\nNew Document\n')

    if key == ("t"):
      print ("\n\n" + document)

    if key == ("e"):
      document = document + input(document)

    if key == ("c"):
      cpassword = input('Type a new password: ')
      ccode = input('Type a new security code')

    if key == ("r"):
      restart = ("1")
    

  
    
