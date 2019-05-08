import os
import csv
import re
countries = []
countriesfl = []
scorefl = []
scorerun = 0
scorerunlist = []
countriescnt = []
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
            score = row[4]
            #add country to a full list to be counted later
            countriesfl.append(country)
            scorefl.append(score)
            #if not blank and not currently on the list of countries, add to that list
            if country not in countries:
                countries.append(country)

#zip the two lists together, then make that zip a list
scorexcount = zip(countriesfl, scorefl)
print(type(scorexcount))
scorexcount = list(scorexcount)
print(type(scorexcount))

for countrycnt in countries:
    scorerun = 0
    count = countriesfl.count(countrycnt)
    countriescnt.append(count)
    for lines in scorexcount:
        if lines[0] != countrycnt:
            continue
        else:
            if lines[1] != "":
                scorecur = float(lines[1])
                scorerun = scorerun + scorecur
    scorerunlist.append(scorerun/count)

roster = zip(countries, countriescnt, scorerunlist)

output_file = os.path.join('.', 'output', 'wine_country.csv')

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Country", "Count", "Average Score"])

    writer.writerows(roster)
