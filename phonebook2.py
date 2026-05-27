name, number
import csv
with open("phonebook.csv","a") as file:
    writer = csv.writer(file)
    writer.writerow([csv.argv[1], csv.argv[2]])
