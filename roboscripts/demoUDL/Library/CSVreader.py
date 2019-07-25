import csv

def open_csv_file_from_device(filename):
    file = open(filename, mode='r')
    return file

def read_first_line_from_device(fileObj):
    csv_reader = csv.reader(fileObj)
    for line in csv_reader:
        return line

def close_csv_file_from_device(fileObj):
    fileObj.close()