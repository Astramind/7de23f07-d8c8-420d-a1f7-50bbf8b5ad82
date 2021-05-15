import csv;
csv_file = csv.reader(open('scv_folder/Stocks_Data_5_years.csv'), delimiter=",");
csv_list = list(csv_file)


def sortByName():
    sort_csv = sorted(csv_list[1:], key= lambda x: x[-1], reverse=True);
    return sort_csv

print(sortByName())

def sortByInput():
    name = input('Enter Comapany Name')
    for row in csv_list:
        if row[-1] == name:
            sort_name = sorted(row, key= lambda x: x[5], reverse=False)
            print(sort_name)


def maxCloseByCompanyDateRange():
    name = input('Enter comapny Name')
    start_Date = input('starting date: ')
    end_Date = input('end date: ')
    for row in csv_list:
        if row[-1] == name:
            if row[0] >= start_Date:
                if row[0] <= end_Date:
                    print(max(float(row[4])))



def voletileStockDate():
    date = input('Enter Date:')
    for row in csv_list:
        max =0
        if date == row[0]:
            if abs(int(row[4])- int(row[1])) > max:
                max = abs(int(row[4]) - int(row[1]))
        print(max)                
