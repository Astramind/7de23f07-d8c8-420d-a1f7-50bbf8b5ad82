import csv;
csv_file = csv.reader(open('scv_folder/Stocks_Data_5_years.csv'), delimiter=",");
csv_list = list(csv_file)


def sortByName():
    sort_csv = sorted(csv_list[1:], key= lambda x: x[-1], reverse=False);
    return sort_csv


def sortByInput():
    name = input('Enter Comapany Name: ')
    for row in csv_file:
        if name == row[6]:
            sort_name = sorted(row[1:], key= lambda x:int(x[5]), reverse=True)
            print(sort_name, end='\n')
 



def maxCloseByCompanyDateRange():
    name = input('Enter comapny Name: ')
    start_Date = input('starting date: ')
    end_Date = input('end date: ')
    for row in csv_file:
        if row[-1] == name:
            if row[0] >= start_Date:
                if row[0] <= end_Date:
                    value = max(float(row[4]))
                    if value == row[4]:
                        return row[4]   
                    
 
print(maxCloseByCompanyDateRange()) 

def voletileStockDate():
    date = input('Enter Date:')
    for row in csv_file:
        max =0
        if date == row[0]:
            if abs(int(row[4])- int(row[1])) > max:
                max = abs(int(row[4]) - int(row[1]))
            else:
                max = max;              
        if max == abs(int(row[4]) - int(row[1])):
            return row

