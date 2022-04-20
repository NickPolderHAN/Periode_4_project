def open_file(given_file):
    """
    Opens the given file in read-only and returns it. The file
    gets closed in the main function.

    :param given_file: String -> contains the file_path.
    :return: file_contents -> String -> contains the file contents.
    """
    file_contents = open(given_file)

    return file_contents


def filter_file_data(file_contents):
    """
    Filters and appends the given file's data to a list and then
    appends these lists to a 2D list.

    :param file_contents: contains file contents
            from the open_file function.
    :return: lines_2d_list -> list -> contains lists with file values.
    """
    # loops over through the lines of the given files,
    # splits them on ";" and appends these lists to a 2D list.
    lines_2d_list = []

    for line in file_contents:
        line = line.strip()
        splitted_value_list = line.split(";")
        lines_2d_list.append(splitted_value_list)

    return lines_2d_list


def store_file_data(lines_2d_list):
    pass


def main():
    # path to the dataset file.
    file_path = "Dataset periode 4 project.csv"

    # calls the function to open the file and return it's
    # contents as a String.
    file_contents = open_file(file_path)

    # calls the function to filter all the data
    # from the given file contents.
    lines_2d_list = filter_file_data(file_contents)

    store_file_data(lines_2d_list)


main()
