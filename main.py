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
            registred_email = str(input('Enter the email address you registered on this website: '))
            registred_password = str(input('Enter the password you entered: '))

            manage_accounts.save_account(
                accounts_folder_path,
                website_name,
                username,
                registred_email,
                registred_password)

            os.system("clear||cls")
            print('Account registered successfully!')
            
        case 2:
            print('Saved accounts: ')

            try:
                files_count = utils.list_and_enumerate_files(accounts_folder_path)
                if files_count == -1:
                    raise FileNotFoundError()

                while True:
                    print()
                    website_number = utils.validate_number(
                        'Enter the number of the site you want to see your account details for: ')

                    if website_number <= files_count and website_number >= 0:
                        break

                    print('Enter a valid number!')
                    
                os.system("clear||cls")
                manage_accounts.read_accounts(accounts_folder_path, website_number)
            except FileNotFoundError:
                print('Register an account to view registered accounts', '\n')
            
        case 3:
            try:
                files_count = utils.list_and_enumerate_files(accounts_folder_path)
                if files_count == -1:
                    raise FileNotFoundError()

                while True:
                    print()
                    website_number = utils.validate_number(
                        'Enter the number of the site you want to delete your account data from: ')

                    if website_number <= files_count and website_number >= 0:
                        break

                    print('Enter a valid number!')

                manage_accounts.delete_accounts(
                    accounts_folder_path,
                    website_number)
                os.system("clear||cls")
                print('Account data log successfully deleted', '\n')
            except FileNotFoundError:
                print('Register an account to delete a registred account', '\n')
        case 4:
            break
    input('Press ENTER.')
    os.system("clear||cls")

print('\n', 'Come back often!')
