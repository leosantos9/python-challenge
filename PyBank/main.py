import os
import csv

budget_csv = os.path.join("..", "PyBank", "budget_data.csv")

rows = []
profit = []
b=[]
aver=0

# Open and read csv
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # counting rows 
    next(csvreader)
    for row in csvreader:
        rows.append(row[0])
        profit.append(int(row[1]))
          
for i in range(len(profit)-1):
    b.append(profit[i+1]-profit[i])

aver = round(sum(b) / (len(profit)-1),2)
month_count = len(rows)
total_profit = sum(profit)
minimo = min(b)
maximo = max(b)
alfa = b.index(maximo)
beta = b.index(minimo)
maxmonth = rows[alfa+1]
minmonth = rows[beta+1]

print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {str(month_count)}")
print(f"Total: ${(total_profit)}")
print(f"Average  Change: ${(aver)}")
print(f"Greatest Increase in profits: {maxmonth}, (${maximo})")
print(f"Greatest Decrease in profits: {minmonth}, (${(minimo)})")

output_path = os.path.join("..", "PyBank", "new.txt")

with open(output_path, 'w', newline='') as datafile:

    csvwriter = csv.writer(datafile, delimiter=',')

    csvwriter.writerow([(f"Financial Analysis")])
    csvwriter.writerow([(f"----------------------------")])
    csvwriter.writerow([(f"Total Months: {str(month_count)}")])
    csvwriter.writerow([(f"Total: ${(total_profit)}")])
    csvwriter.writerow([(f"Average  Change: ${(aver)}")])
    csvwriter.writerow([(f"Greatest Increase in profits: {maxmonth} (${maximo})")])
    csvwriter.writerow([(f"Greatest Decrease in profits: {minmonth} (${(minimo)})")])
