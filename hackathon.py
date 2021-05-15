import csv;
csv_file = csv.reader(open('scv_folder/Stocks_Data_5_years.csv'), delimiter=",");
csv_list = list(csv_file)


def sortByName():
    sort_csv = sorted(csv_list[1:], key= lambda x: x[-1])
    return sort_csv

print(sortByName())

def sortByInput():


