from sys import argv

import csv

with open("phonebook.csv","a") as file:
    writer = csv.writer(file)
    writer.writerow([argv[1],argv[2]])
