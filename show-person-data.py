import csv
import os
from glob import glob

person_list = {}
field_length = {}

def print_separator_line(): 
  for field in field_length:
    print('+' + '-' * (field_length[field]+1), end="")
  print('+')

# Find alle underbiblioteker. Find filen person-data.csv og indlæs den
for path in [d for d in os.listdir('.') if os.path.isdir(d)]:
  file_name = os.path.join(path,"person-data.csv")
  if not os.path.isfile(file_name): continue

  with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',',skipinitialspace=True)
    person_entry = {}
    for row in csv_reader:
      if len(row) >= 2:
        person_entry[row[0]] = row[1]
    person_list[os.path.basename(path[0:-1])] = person_entry

# Find de længste ord, i hver kategori
for dir_name in person_list:
  person = person_list[dir_name]
  for field in person:
    if not field in field_length or field_length[field] < len(person[field]):
      field_length[field] = len(person[field])

# Skriv header
print_separator_line()
for field in field_length:
  print(str("| {:"+str(field_length[field])+"}").format(field.capitalize()), end = '')
print("|")
print_separator_line()

# skriv indhold
for dir_name in person_list:
  person = person_list[dir_name]
  for field in field_length:
    if field in person:
      string = person[field]
    else:
      string = ""      
    print(str("|{:"+str(field_length[field]+1)+"}").format(string), end = '')
  print("|")

print_separator_line()
