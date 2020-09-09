import csv
import os
import pprint
from glob import glob

person_list = list()
pp = pprint.PrettyPrinter(width=41, compact=True)

for path in glob("./*/"):
  file_name = os.path.join(path,"person-data.csv")
  print(file_name)
  if not os.path.isfile(file_name): continue

  with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    person_entry = dict()
    for row in csv_reader:
      if len(row) >= 2:
        person_entry[row[0]] = row[1]
    person_list.append(person_entry)


for person in person_list:

    pp.pprint([person['name'],person['git name'],person['email']])
#        if line_count == 0:
#            print(f'Column names are {", ".join(row)}')
#            line_count += 1
#        else:
#            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#            line_count += 1
#    print(f'Processed {line_count} lines.')
