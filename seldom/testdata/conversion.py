"""
Data type conversion of different files
"""
import csv
import codecs
from itertools import islice


def csv_to_list(file=None, line=None):
    """
    Convert CSV file data to list
    :param file: Path to file
    :param line: Start line of read data, default to start at line 0
    :return:  list data
    """
    if file is None:
        raise FileExistsError("Please specify the CSV file to convert.")

    if line is None:
        line = 0

    data_list = []
    csv_data = csv.reader(codecs.open(file, 'r', 'utf_8_sig'))
    for line in islice(csv_data, line, None):
        data_list.append(line)

    return data_list
