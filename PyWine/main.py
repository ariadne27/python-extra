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
        #make sure the country element is not black
        if row[1] != "":
            country = row[1]
            #add country to a full list to be counted later
            countriesfl.append(country)
            #if not blank and not currently on the list of countries, add to that list
            if country not in countries:
                countries.append(country)
            # variety = row[9]    
            # if variety not in varieties:
            #     varieties.append(variety)
#for each element in counties, count the number of times that element appears on the full list
#add that number to a count list in the same position as the country it collelates to
for countrycnt in countries:
    count = countriesfl.count(countrycnt)
    countriescnt.append(count)
#for each element in the countries list, print the element and the corresponding count valueS
for countryf in countries:
    print(str(countryf) + ": " + str(countriescnt[increase]))
    increase = increase + 1