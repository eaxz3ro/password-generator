import random
import array
import os
print("Hey",os.getlogin(),", welcome to Passgen")
def generate():
    NUM = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LCASE_CHAR = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    UCASE_CHAR = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
    SYM = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']

    TOTAL_LIST = NUM + UCASE_CHAR + LCASE_CHAR + SYM
    r_digit = random.choice(NUM)
    r_upper = random.choice(UCASE_CHAR)
    r_lower = random.choice(LCASE_CHAR)
    r_symbol = random.choice(SYM)

    temp_pass = r_digit + r_upper + r_lower + r_symbol
    length = int(input("Enter the length of password you want:"))
    for x in range(length-4):
	    temp_pass = temp_pass + random.choice(TOTAL_LIST)

    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
	    password = password + x
    print(password)
    site=input("Which site do you want to use the password for? ")
    website=site
    f=open('pass.txt','a')
    f.write(website+" : "+password+"\n")
    f.close
    print("Saved to file pass.txt")
    choice=input("Would you like to generate password again?[y/n] ")
    if(choice=='y' or choice=='Y'):
        generate()
    else:
        print("Exiting now!")
generate()
