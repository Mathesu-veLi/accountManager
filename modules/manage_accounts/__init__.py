import os
import json
from ..utils import custom_validate_number

def save_account(account_folder_path: str, website_name: str, username: str, registered_email: str, registered_password: str):
    """Saves the account data in a json file with the name of the website where the account was registered

    Args:
        account_folder_path (str): Name of the folder in which the account is saved
        website_name (str): name of the website where the account was created
        username (str): name of the user registered on the site
        registered_email (str): email address registered on the site
        registered_password (str): password registered on the site
    """

    data_registered_on_the_website = {
        username: {
            'email': registered_email,
            'password': registered_password
        },
    }
    

    openTextMode: str;
    try:
        os.mkdir(account_folder_path)
        with open(f'{account_folder_path}/{website_name}.json', 'w', encoding='utf-8') as file:
            json.dump(data_registered_on_the_website, file)
    except FileExistsError:
        with open(f'{account_folder_path}/{website_name}.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            data[website_name][username] = {
                'email': registered_email,
                'password': registered_password
            }
            with open(f'{account_folder_path}/{website_name}.json', 'w', encoding='utf-8') as file:
                json.dump(data, file)
        

def show_accounts(account_folder_path: str, website_number: int):
    """Shows the accounts of a specific website
    
    Args:
        account_folder_path (str): Path to search for account files
        website_number (int): Number that the website appears in the file search system, used to identify it
    """
    website_name = None
    data = None
    for iterator, file_name in enumerate(os.listdir(account_folder_path)):
        if iterator == website_number:
            website_name = file_name.removesuffix('.json')
            
            with open(f'{account_folder_path}/{file_name}', 'r', encoding='utf-8') as file:
                data = json.load(file)

                for iterator, key in enumerate(data.keys()):
                    print(f"{iterator}: {key}")
                    
                    
    account_number = custom_validate_number('Enter the number of the site you want to see your account details for: ', iterator)
    
    account_data = get_account(data, account_number)
    show_account(account_data[0], website_name, account_data[1])

def show_account(data, website_name, username):
    """Shows the account details of a specific user
    
    Args:
        data (dict): Dictionary containing the account data
        website_name (str): Name of the website where the account was created
        username (str): Name of the user registered on the site
    """
    print('\n', f"{website_name} - {username}".center(55))
    print(data['email'].ljust(35), end='')
    print(data['password'].rjust(20), '\n')
    
def get_account(data, account_number: int):
    """Retrieves the account data for a specific user
    
    Args:
        data (dict): Dictionary containing the account data
        account_number (int): The number of the account to retrieve
    Returns:
        tuple: Tuple containing the account data and the username
        If the account number does not exist, it returns None and an empty string
    """
    
    account_data = None
    username = ""
    for iterator, key in enumerate(data.keys()):
        if (iterator == account_number):
            username = key
            account_data = data[key]
            
    return [account_data, username]

def delete_accounts(account_folder_path: str, website_number: int):
    """Deletes the json file indicated by website_number

    Args:
        account_folder_path (str): Path to search for account files
        website_number (int): Number that the website appears in the file search system, used to identify it
    """

    for iterator,  file_name in enumerate(os.listdir(account_folder_path)):
        if iterator == website_number:
            os.remove(f'{account_folder_path}/{file_name}')
