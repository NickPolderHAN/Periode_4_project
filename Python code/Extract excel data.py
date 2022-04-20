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
    """
    Processes the given 2d_list and appends
    these to a dictionary with he first item
    from these lists as it's key.

    :param lines_2d_list: List:
                contains lists with file values
                from the filter_file function.

    :return: dataset_dictionary -> Dict:
                a dictionary containing the 2d list it's contents
                with the first item from these lists as it's key.
    """

    dataset_dictionary = {}

    # loops through the lists in the 2d list
    for list_item in lines_2d_list:
        # takes the first item as a header and makes it
        # into a dictionary key containing an empty list.
        header = list_item[0]
        dataset_dictionary[header] = []

        # loops through the items in the given list and
        # appends them to the dictionary of the given dictionary key.
        for item in list_item:
            if item != header:
                dataset_dictionary[header].append(item)

    return dataset_dictionary


def main():
    # path to the dataset file.
    file_path = "Dataset periode 4 project.csv"

    # calls the function to open the file and return it's
    # contents as a String.
    file_contents = open_file(file_path)

    # calls the function to filter all the data
    # from the given file contents.
    lines_2d_list = filter_file_data(file_contents)

    # calls the function to process the given 2d_list and appends
    # these to a dictionary with he first item from these lists as
    # it's key.
    dataset_dict = store_file_data(lines_2d_list)

    # closes the returned file from the open function.
    file_contents.close()


main()
