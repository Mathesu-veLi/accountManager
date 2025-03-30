import os
from modules import utils, manage_accounts
from time import sleep


print('Welcome to the account manager!', '\n')

while True:
    print('Type 1 to save or update an account')
    print('Type 2 to view saved accounts')
    print('Type 3 to delete an account')
    print('Type 4 to exit the program', '\n')

    option = utils.validate_number('Type an option: ')
    while option > 4 or option < 1:
        print('Type a number from 1 to 3')
        option = utils.validate_number('Type an option: ')
    os.system("clear||cls")

    accounts_folder_path = os.path.join('./', 'accounts')

    match(option):
        case 1:
            website_name = str(input('Enter the name of the website where you registered your account: '))
            username = str(input('Enter a name to the user: '))
            registered_email = str(input('Enter the email address you registered on this website: '))
            registered_password = str(input('Enter the password you entered: '))

            manage_accounts.save_account(
                accounts_folder_path,
                website_name,
                username,
                registered_email,
                registered_password)

            os.system("clear||cls")
            print('Account registered successfully!')
            
        case 2:
            try:
                files_count = utils.list_and_enumerate_files(accounts_folder_path)
                
                website_number = utils.custom_validate_number('Enter the number of the site you want to see your account details for: ', files_count)
                    
                os.system("clear||cls")
                manage_accounts.show_accounts(accounts_folder_path, website_number)
            except FileNotFoundError:
                print('Register an account to view registered accounts', '\n')
            
        case 3:
            try:
                files_count = utils.list_and_enumerate_files(accounts_folder_path)

                website_number = utils.custom_validate_number('Enter the number of the site you want to see your account details for: ', files_count)

                manage_accounts.delete_accounts(
                    accounts_folder_path,
                    website_number)
                os.system("clear||cls")
                print('Account data log successfully deleted', '\n')
            except FileNotFoundError:
                print('Register an account to delete a registered account', '\n')
        case 4:
            break
    input('Press ENTER.')
    os.system("clear||cls")

print('\n', 'Come back often!')
