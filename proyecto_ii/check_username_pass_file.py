import os
import sys


#Checking username/password file
#Prompting user for input - USERNAME/PASSWORD FILE
user_file = input("\n# Enter user file path and name (e.g. D:\MyApps\myfile.txt): ")

#Verifying the validity of the USERNAME/PASSWORD file
if os.path.isfile(user_file) == True:
    print("\n* Username/password file is valid :)\n")

else:
    print("\n* File {} does not exist :( Please check and try again.\n".format(user_file))
    sys.exit() 





