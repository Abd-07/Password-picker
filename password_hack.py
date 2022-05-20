'''import random

#4 Lists of numbers from 0 to 9:
first_digit=[0,1,2,3,4,5,6,7,8,9]

while True:

    #Random Choice of a number    
    first_password_generator=random.choice(first_digit)

    #The print of the final combination of 4 numbers
    password=print(f"{first_password_generator}")

    #List where all the generated passwords are stored
    generated_passwords=[]

    #After that a password is generated it goes to the list of generated passwords
    generated_passwords.append(password)

    #If the combination that is generated has already been generated previously then the cycle breaks
    if password in generated_passwords:
        generated_passwords.remove(password)'''

import random
from re import I
import openpyxl

#4 Lists of numbers from 0 to 9:
number_list=[0,1,2,3,4,5,6,7,8,9]
def generate_passwords():
    passwords=[]
    i=0
    while i <= 100:
        password=f"{random.choice(number_list)}{random.choice(number_list)}{random.choice(number_list)}{random.choice(number_list)}"
        if password not in passwords:
            passwords.append(password)
            i += 1
            print(i)
    return passwords
def write_pass_in_excel():
    book=openpyxl.Workbook()
    sheet=book.active
    passwords=generate_passwords()
    sheet['A1']="Passwords"
    for i in range(len(passwords)):
        sheet[f'A{i+2}']=passwords[i]
    book.save('all_passwords.xlsx')
    book.close()
write_pass_in_excel()

'''while True:
    book=openpyxl.Workbook()
    sheet=book.active
    sheet['A1']="Passwords"
    #Random Choice of a number  
    
    f_pa_gen=random.choice(number_list)
    
    s_pa_gen=random.choice(number_list)
    
    t_pa_gen=random.choice(number_list)
    
    fou_pa_gen=random.choice(number_list)

    
    #The print of the final combination of 4 numbers
    password=f"{f_pa_gen}{s_pa_gen}{t_pa_gen}{fou_pa_gen}"
    print(password)
    sheet[f'A{counter}']=password
    counter += 1
    book.save('my_book.xlsx')

    if counter == 100:
        book.close()
        break
    #List where all the generated passwords are store
    

    #After that a password is generated it goes to the list of generated passwords
    
    

    #If the combination that is generated has already been generated previously then the cycle breaks'''
