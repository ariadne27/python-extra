import os
import csv
import re
countries = []
countriesfl = []
countriescnt = []
varieties = []
increase = 0
count0 = 0
csvpath = os.path.join('.', 'resources', 'wine_data8.csv')
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

     # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
         #save row elements to variables
        if row[1] != "":
            country = row[1]
            countriesfl.append(country)
            if country not in countries:
                countries.append(country)
            # variety = row[9]    
            # if variety not in varieties:
            #     varieties.append(variety)
for countrycnt in countries:
    count = countriesfl.count(countrycnt)
    countriescnt.append(count)
for countryf in countries:
    print(str(countryf) + ": " + str(countriescnt[increase]))
    increase = increase + 1


# # print(varieties)
# # print(len(varieties))
# with open(csvpath, newline='') as csvfile:
#     # CSV reader specifies delimiter and variable that holds contents
#     csvreader = csv.reader(csvfile, delimiter=',')

#      # Read the header row first (skip this step if there is now header)
#     csv_header = next(csvreader)
    
#     # Read each row of data after the header
#     for row in csvreader:
#         if row[1] == countries[0]:
#             count0 = count0 +1
# print(str(countries[0]) + ": " + str(count0))