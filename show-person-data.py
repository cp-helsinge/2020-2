import csv
import os
from glob import glob

person_list = {}

for path in glob("./*/"):
  file_name = os.path.join(path,"person-data.csv")
  if not os.path.isfile(file_name): continue

  with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    person_entry = {}
    for row in csv_reader:
      if len(row) >= 2:
        person_entry[row[0]] = row[1]
    person_list[os.path.basename(path[0:-1])] = person_entry

for dir_name in person_list:
  person = person_list[dir_name]
  print('{:10} {:20} {:15} {}'.format(
      dir_name,
      person['name'],
      person['git name'],
      person['email']
   )
  )

