import random
from tkinter.tix import CELL
from unicodedata import digit
import openpyxl

#List of numbers going from 0 to 9
number_list=[0,1,2,3,4,5,6,7,8,9]
#List of all capital letters
caps_letters=["A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"]
#List of all small letters
small_letters=["a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"]
#List of some special characters
special_characters=[" ","!","-","_","?"]
#List of 4 digit numeric passwords(already generated)
number_passwords=[]
#List of 4 digit strong passwords(already generated)
strong_passwords=[]
#Variable whose value is given in the bracets,in the "write_pass_in_excel__()" function.It helps us understand for which password type we are executing it and eventually makes our code shorter because we don't need to create 2 same functions,with only values being different.
flag=""

#---------------------------------------------------------------------------------------------------

#This function writes our generated password into excel
def write_pass_in_excel__(flag,cell,password_type):
    book=openpyxl.Workbook()
    sheet=book.active
    if flag == 'number':
        passwords=number_passwords
    if flag == 'strong':
        passwords=strong_passwords
    sheet[f'{cell}1']=f"Passwords-{password_type}"
    for i in range(len(passwords)):
        sheet[f'{cell}{i+2}']=passwords[i]
    book.save('all_passwords.xlsx')
    book.close()

#---------------------------------------------------------------------------------------------------

#Genarates 4 digit numeric passwords
def generate_number_passwords():
    global number_passwords
    counter_number_passwords_generated=0
    while counter_number_passwords_generated <= 50:
        password=f"{random.choice(number_list)}{random.choice(number_list)}{random.choice(number_list)}{random.choice(number_list)}"
        if password not in number_passwords:
            number_passwords.append(password)
            counter_number_passwords_generated += 1
            print(f"Counter of NUMERIC passwords generated:{counter_number_passwords_generated}")
    return number_passwords

#Runs the function which generates the password
generate_number_passwords()
#Calls the function which writes the generated passwords in excel,but has critereas
write_pass_in_excel__("number",'A',"4 digit_numeric")

#--  --  --  --  --  --  --  --  --  -- 

#Genarates 4 digit strong passwords
def generate_strong_passwords():
    global strong_passwords
    counter_strong_passwords_generated=0
    while counter_strong_passwords_generated <= 50:
        password=f"{random.choice(caps_letters)}{random.choice(small_letters)}{random.choice(special_characters)}{random.choice(number_list)}"
        if password not in strong_passwords:
            strong_passwords.append(password)
            counter_strong_passwords_generated += 1
            print(f"Counter of STRONG passwords generated:{counter_strong_passwords_generated}")
    return strong_passwords

#Runs the function which generates the password
generate_strong_passwords()
#Calls the function which writes the generated passwords in excel,but has critereas
write_pass_in_excel__("strong",'B',"4 digit_strong")

'''print(number_passwords)
print(strong_passwords)'''