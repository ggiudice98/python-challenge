#Import modules
import os
import csv

#Get the total number of months included in the dataset
with open('Resources/budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = -1
    for line in csv_reader:
         line_count += 1
      
#Get the net total amount of Profit/Losses over the entire period
with open('Resources/budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    profit = 0
    for index, row in enumerate(csv_reader):
      if index > 0:
        profit += int(row[1])


#Get a list of all the change dates
with open('Resources/budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    change_dates = []
    for index, row in enumerate(csv_reader):
        if index > 1:
            change_dates.append(row[0])

#Get a list of all the change amounts
with open('Resources/budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    change_amounts = []
    for index, row in enumerate(csv_reader):
        if index == 1:
            old_value = int(row[1])
        elif index > 1:
            new_value = int(row[1])
            change = new_value - old_value
            change_amounts.append(change)
            old_value = new_value


#Get the greatest increase in profit
greatest_increase_amt = max(change_amounts)

#Get the index of the greatest increase in profit
greatest_increase_index = change_amounts.index(greatest_increase_amt)

#Get the date of the greatest increase in profit
greatest_increase_date = change_dates[greatest_increase_index]

#Get the greatest decrease in profit
greatest_decrease_amt = min(change_amounts)

#Get the index of the greatest decrease in profit
greatest_decrease_index = change_amounts.index(greatest_decrease_amt)

#Get the date of the greatest decrease in profit
greatest_decrease_date = change_dates[greatest_decrease_index]


def Average(lst):
    return sum(lst) / len(lst)
average_change = Average(change_amounts)

#Print to Terminal
print("Financial Analysis")
print('-' * 40)
print(f"Total Months: {line_count}")
print(f"Total: ${profit}")
print(f"Average Change: ${round(average_change,2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amt})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amt})")

#Print to File
output_file_path = 'financial_analysis.txt'

# Open the output file in write mode
with open(output_file_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write('-' * 28 + "\n")
    output_file.write(f"Total Months: {line_count}\n")
    output_file.write(f"Total: ${profit}\n")
    output_file.write(f"Average Change: ${round(average_change, 2)}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amt})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amt})\n")