import csv

lista = []
total = 0

with open('KCPD_Crime_data_2019 copy.csv') as csv_file:
  reader = csv.reader(csv_file)
  


  for row in reader:
      lista.append(row)
  csv_file.close()

lista.sort()
for line in lista:
  total1= row[13]
  print(total1)  
  total += 1

print(total)
   