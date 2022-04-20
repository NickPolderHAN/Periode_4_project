
def open_file(given_file):
    with open(given_file, "r") as file:
        file_contents = file.read()

    return file_contents

def main():
    file_path = "Dataset periode 4 project.csv"
    file_content = open_file(file_path)
    print(file_content)

main()