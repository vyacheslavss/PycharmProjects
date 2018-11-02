file_name = "file.txt"
file="index.html"

def write_to_file():
    input_text = input("Enter your tesxt\n")
    with open(file_name, 'w') as text_file:
        print(input_text, file=text_file)


def write_to_file2():
    input_text = input("Enter your tesxt\n")
    myfile=open(file, 'a')
    myfile.write(input_text)


# write_to_file()
write_to_file2()