import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    reader = csv.reader(csvfile)
   for row in reader:
        month = row[0]
        months.append(month)
        values = int(row[1])
        p.append(values)

total_months = len(months)
net_total = sum(p)
net_total_months = len(months) - 1
difference_budget_data = []

for i in range(len(p) - 1):
    difference_budget_data.append(float(p[i + 1]) - float(p[i]))
    new_net_total = sum(difference_budget_data)

# Find the sum of profits/losses
average_net_change = new_net_total/net_total_months

# Find the greatest increase/decrease (date and amount) over the entire period
min_p = p[p.index(min(p))] - p[p.index(min(p))-1]
max_p = p[p.index(max(p))] - p[p.index(max(p))-1]

# Print out results to console
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(average_net_change,2)}")
print(f'Greatest Increase in Profits: {months[p.index(max(p))]} (${max_p})')
print(f"Greatest Descrease in Profits: {months[p.index(min(p))]} (${min_p})")
