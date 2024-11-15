#!/usr/bin/python3
import sys


def print_msg(dict_sc, total_file_size):
    """
    Prints the total file size and the count of HTTP
    status codes encountered in the input.
    This function takes a dictionary of HTTP
    status codes and their corresponding counts,
    along with the total file size, and formats
    them for display. It first outputs the total
    file size, followed by a sorted list of
    status codes that have occurred at least once.
    Args:
        dict_sc (dict): A dictionary where the keys
        are HTTP status codes as strings
        and the values are the number of occurrences for each status code.
        total_file_size (int): The total size of the
        files, accumulated from input.
    Returns:
        None: This function prints the output
        directly and does not return any value.
    """

    print("File size: {}".format(total_file_size))  # Display total file size
    for key, val in sorted(dict_sc.items()):
        if val != 0:  # Only print status codes that appeared in the input
            print("{}: {}".format(key, val))  # Display the status code


total_file_size = 0
code = 0
counter = 0
dict_sc = {
    "200": 0,  # OK
    "301": 0,  # Moved Permanently
    "400": 0,  # Bad Request
    "401": 0,  # Unauthorized
    "403": 0,  # Forbidden
    "404": 0,  # Not Found
    "405": 0,  # Method Not Allowed
    "500": 0   # Internal Server Error
}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])
                code = parsed_line[1]

                if code in dict_sc:
                    dict_sc[code] += 1

            if counter == 10:
                print_msg(dict_sc, total_file_size)
                counter = 0

finally:
    print_msg(dict_sc, total_file_size)
