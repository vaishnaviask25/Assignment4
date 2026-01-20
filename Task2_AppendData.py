filename = "C:\\Users\\vaish\\.spyder-py3\\Python files\\tutedude_Assignments\\output.txt"

def file_open():
    opening_text = input("Enter text to write to the file: ")
    with open(filename, "wt") as fh:
        fh.write(f"{opening_text} \n")
    print("Data successfully written to output.txt.\n")

    additional_text = input("Enter additional text to append: ")
    with open(filename, "at") as fh:
        fh.write(f"{additional_text} \n")
    print("Data successfully appended.\n")

    print("Final content of output.txt:")
    with open(filename, "rt") as fh:
        content = fh.read()
    print(content)

file_open()