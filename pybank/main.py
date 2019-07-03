import os
import csv

budget_file = os.path.join("budget_data.csv")

with open(budget_file, newline="") as csvfile:
  csv_reader = csv.reader(csvfile, delimiter=",")

  csv_header = next(csvfile)
  months = 0
  net_total = 0
  changes = 0.0
  increase = 0.0
  inc_month = ''
  decrease = 0.0
  dec_mon = ''

  # Read through each row of data after the header
  for row in csv_reader:
    months += 1
    net_total += int(row[1])
    if float(row[1]) > increase:
      increase = int(row[1])
      inc_month = row[0]

    if float(row[1]) < decrease:
      decrease = int(row[1])
      dec_month = row[0]

  changes = net_total/months
  anal_head = "Financial Analysis"
  anal_months = f"Total Months: {months}"
  anal_net = f"Total: ${'{:7,.2f}'.format(net_total)}"
  anal_change = f"Average Change: ${'{:7,.2f}'.format(changes)}"
  anal_inc = f"Greatest Increase in Profits: {inc_month} (${'{:7,.2f}'.format(increase)})"
  anal_dec = f"Greatest Decrease in Profits: {dec_month} (${'{:7,.2f}'.format(decrease)})"

  print(anal_head)
  print(anal_months)
  print(anal_net)
  print(anal_change)
  print(anal_inc)
  print(anal_dec)

# Specify the file to write to
file_path = os.path.join("analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(file_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow([anal_head])
    csvwriter.writerow([anal_months])
    csvwriter.writerow([anal_net])
    csvwriter.writerow([anal_change])
    csvwriter.writerow([anal_inc])
    csvwriter.writerow([anal_dec])
