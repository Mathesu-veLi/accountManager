import os
import json


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
        website_name: {
            username: {
                'email': registered_email,
                'password': registered_password
            },
        },
    }

    openTextMode: str;
    try:
        os.mkdir(account_folder_path)
    except FileExistsError:
        pass
    finally:
        with open(f'{account_folder_path}/{website_name}.json', 'w', encoding='utf-8') as file:
            json.dump(data_registered_on_the_website, file)


def read_accounts(account_folder_path: str, website_number: int):
    """Reads the json file indicated by website_number

    Args:
        account_folder_path (str): Path to search for account files
        website_number (int): Number that the website appears in the file search system, used to identify it
    """

    for iterator,  file_name in enumerate(os.listdir(account_folder_path)):
        if iterator == website_number:
            with open(f'{account_folder_path}/{file_name}', 'r', encoding='utf-8') as file:
                data = json.load(file)

                print('\n', f"{data['website']} - {data['username']}".center(55))
                print(data['email'].ljust(35), end='')
                print(data['password'].rjust(20), '\n')


def delete_accounts(account_folder_path: str, website_number: int):
    """Deletes the json file indicated by website_number

    Args:
        account_folder_path (str): Path to search for account files
        website_number (int): Number that the website appears in the file search system, used to identify it
    """

    for iterator,  file_name in enumerate(os.listdir(account_folder_path)):
        if iterator == website_number:
            os.remove(f'{account_folder_path}/{file_name}')
