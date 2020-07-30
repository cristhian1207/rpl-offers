import csv

def writeCsv(filename, rows, fieldnames):
  with open(f'data/{filename}', mode='w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter = ';', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(rows)