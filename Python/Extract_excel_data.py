

def filter_file_data(file_path):
    """
    Opens, filters and appends the given file's data to a list and then
    appends these lists to a 2D list.

    :param: file_path -> String -> Contains the file path to the
                                    file which needs to be read.

    :return: lines_2d_list -> list -> contains lists with file values.
    """
    # opens the file at the given file_path
    file_contents = open(file_path)

    # loops over through the lines of the given files,
    # splits them on ";" and appends these lists to a 2D list.
    lines_2d_list = []

    # loops over the file_contents its lines, splits them on ';' and
    # appends them to a 2D list.
    for line in file_contents:
        line = line.strip()
        splitted_value_list = line.split(";")
        lines_2d_list.append(splitted_value_list)

    file_contents.close()
    return lines_2d_list


def store_file_data(lines_2d_list):
    """
    Processes the given 2d_list and appends
    these to a dictionary with the first item
    from these lists as it's key.

    :param lines_2d_list: List:
                contains lists with file values
                from the filter_file function.

    :return: dataset_dictionary -> Dict:
                a dictionary containing the 2d list it's contents
                with the first item from these lists as it's key.
    """

    # creates the dictionary which holds the 2D list its items with
    # a unique id as their keys.
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

    # calls the function to filter all the data
    # from the given file contents.
    lines_2d_list = filter_file_data(file_path)

    # calls the function to process the given 2d_list and appends
    # these to a dictionary with the first item from these lists as
    # its key.
    dataset_dict = store_file_data(lines_2d_list)

    # passes the dictionary to the main script.
    return dataset_dict
