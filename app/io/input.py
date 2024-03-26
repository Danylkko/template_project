import pandas as pd

def read_user_input():
    """
    Reads user input from the console.

    Returns:
        str: The string entered by the user.
    """
    user_input = input("Enter your input: ")
    return user_input

def read_file_default(path):
    """
    Reads the contents of a file using standard Python functions.

    Args:
        path (str): The path to the file to be read.

    Returns:
        str: The contents of the file as a string.
    """
    with open(path, 'r') as file:
        return file.read()

def read_file_pandas(path):
    """
    Reads the contents of a file using the pandas library.

    Args:
        path (str): The path to the file to be read.

    Returns:
        DataFrame: The data from the file as a pandas DataFrame.
    """
    file_content = pd.read_csv(path)
    return file_content