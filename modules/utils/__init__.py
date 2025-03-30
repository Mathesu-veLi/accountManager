from os import listdir


def validate_number(ask):
    """Checks if the value is a number and returns it if it is

    Args:
        ask (str): question that will go in the input

    Returns:
        float: number in float
    """
    
    while True:
        try:
            number = float(input(ask))
            return number
        except ValueError:
            print('Enter a valid number!', '\n')

def custom_validate_number(ask, max_number):
    """Checks if the value is a number between 0 and max_number (inclusive) and returns it if it is

    Args:
        ask (str): question that will go in the input
        max_number (int): maximum allowed value
    Returns:
        int: number in integer
    Raises:
        RuntimeError: if the input is -1
    """
    while True:
        print()
        number = validate_number(ask)

        if number <= max_number and number >= 0:
            return number;
        if number == -1:
            raise RuntimeError

        print('Enter a valid number!')
        

def list_and_enumerate_files(path):
    """Reads files from the given path, enumerates them and returns the number of files in the path

    Args:
        path (str): Path where the function will look for the files

    Returns:
        int: number of files in the path
    """
    files_count = -1

    for iterator, file_name in enumerate(listdir(path)):
        print(f"{iterator}: {file_name.replace('.json', '')}")
        files_count += 1
    
    if files_count == -1:
        raise FileNotFoundError()

    return files_count

