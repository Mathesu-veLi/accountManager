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


def list_and_enumerate_files(path):
    """Reads files from the given path, enumerates them and returns the number of files in the path

    Args:
        path (str): Path where the function will look for the files

    Returns:
        int: number of files in the path
    """
    files_count = -1

    for iterator, file_name in enumerate(listdir(path)):
        print(f'{iterator}: {file_name.replace('.json', '')}')
        files_count += 1

    return files_count
