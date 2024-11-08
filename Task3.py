#Write a Python program that opens a file and handles a FileNotFoundError exceptionif the file does not exist.


def open_file(file_name):
    """
    Opens a file and returns its content.
    
    Args:
        file_name (str): The name of the file to be opened.
    
    Returns:
        str: The content of the file.
    
    Raises:
        FileNotFoundError: If the file does not exist.
    """
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
        return None

# Example usage:
file_name = "story.txt"
content = open_file(file_name)

if content is not None:
    print(content)
