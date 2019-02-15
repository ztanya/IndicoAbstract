import csv


def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=':')
    for line in reader:
        print(line["oldaffiliation"] + ":" + line["newaffiliation"])


if __name__ == "__main__":
    with open("matches.csv") as f_obj:
        csv_dict_reader(f_obj)