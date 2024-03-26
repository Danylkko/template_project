def output_to_console(text):
    """
    Outputs text to the console.

    Args:
        text (str): The text to be output.
    """
    print(text)
    return

def output_to_file(text, to_path):
    """
    Writes text to a file.

    Args:
        text (str): The text to be written.
        to_path (str): The path to the file where the text should be written.
    """
    with open(to_path, 'w') as file:
        file.write(text)