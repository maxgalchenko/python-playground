def read_file_contents(file_path):
    try:
        with open(file_path, "r") as file:
            print(file)
    except FileNotFoundError:
        print(f"File is not found. E:{file_path}")


file = "/Users/Example/Documents/my_file.txt"
read_file_contents(file)


def read_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")