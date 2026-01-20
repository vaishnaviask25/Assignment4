filename = "C:\\Users\\vaish\\.spyder-py3\\Python files\\tutedude_Assignments\\sample.txt"
try:
    with open(filename, 'rt') as fh:
        print("Reading file content:")
        for i, line in enumerate(fh, start=1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The file {filename} was not found.")